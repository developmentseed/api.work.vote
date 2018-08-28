import os
import json
import rasterio
from math import ceil
from rasterio.transform import Affine
from rasterio.coords import disjoint_bounds

from django.conf import settings
from django.core.management.base import BaseCommand

from jurisdiction.models import Jurisdiction


def rasterize(
        geojson,
        output,
        like=None,
        bounds=None,
        dimensions=None,
        res=None,
        src_crs=None,
        all_touched=None,
        default_value=1,
        fill=0,
        prop=None,
        force_overwrite=None,
        creation_options={},
        driver='GTiff'):

    from rasterio._base import is_geographic_crs, is_same_crs
    from rasterio.features import rasterize
    from rasterio.features import bounds as calculate_bounds

    has_src_crs = src_crs is not None
    src_crs = src_crs or 'EPSG:4326'

    # If values are actually meant to be integers, we need to cast them
    # as such or rasterize creates floating point outputs
    if default_value == int(default_value):
        default_value = int(default_value)
    if fill == int(fill):
        fill = int(fill)

    with rasterio.drivers():

        def feature_value(feature):
            if prop and 'properties' in feature:
                return feature['properties'].get(prop, default_value)
            return default_value

        if 'features' in geojson:
            geometries = []
            for f in geojson['features']:
                geometries.append((f['geometry'], feature_value(f)))
        elif 'geometry' in geojson:
            geometries = ((geojson['geometry'], feature_value(geojson)), )
        else:
            raise Exception

        geojson_bounds = geojson.get('bbox', calculate_bounds(geojson))

        if like is not None:
            template_ds = rasterio.open(like)

            if has_src_crs and not is_same_crs(src_crs, template_ds.crs):
                raise Exception

            if disjoint_bounds(geojson_bounds, template_ds.bounds):
                print('GeoJSON outside bounds of --like raster.')

            kwargs = template_ds.meta.copy()
            kwargs['count'] = 1

            # DEPRECATED
            # upgrade transform to affine object or we may get an invalid
            # transform set on output
            kwargs['transform'] = template_ds.affine

            template_ds.close()

        else:
            bounds = bounds or geojson_bounds

            if is_geographic_crs(src_crs):
                if (bounds[0] < -180 or bounds[2] > 180 or
                        bounds[1] < -80 or bounds[3] > 80):
                    raise Exception

            if dimensions:
                width, height = dimensions
                res = (
                    (bounds[2] - bounds[0]) / float(width),
                    (bounds[3] - bounds[1]) / float(height)
                )

            else:
                if not res:
                    raise Exception

                elif len(res) == 1:
                    res = (res[0], res[0])

                width = max(int(ceil((bounds[2] - bounds[0]) /
                            float(res[0]))), 1)
                height = max(int(ceil((bounds[3] - bounds[1]) /
                             float(res[1]))), 1)

            src_crs = src_crs.upper()
            if not src_crs.count('EPSG:'):
                raise Exception

            kwargs = {
                'count': 1,
                'crs': src_crs,
                'width': width,
                'height': height,
                'transform': Affine(res[0], 0, bounds[0], 0, -res[1],
                                    bounds[3]),
                'driver': driver
            }
            kwargs.update(**creation_options)

        result = rasterize(
            geometries,
            out_shape=(kwargs['height'], kwargs['width']),
            transform=kwargs.get('affine', kwargs['transform']),
            all_touched=all_touched,
            dtype=kwargs.get('dtype', None),
            default_value=default_value,
            fill = fill)

        if 'dtype' not in kwargs:
            kwargs['dtype'] = result.dtype

        kwargs['nodata'] = fill

        with rasterio.open(output, 'w', **kwargs) as out:
            out.write_band(1, result)


class Command(BaseCommand):
    help = 'Generate jurisdiction images'

    def handle(self, *args, **options):

        js = Jurisdiction.objects.all()

        for j in js:
            image = str(settings.BASE_DIR.path('config/static/jurisdictions/%s.png' % j.id))
            image_aux = image + '.aux.xml'

            if not os.path.exists(image):
                obj = {
                    'type': 'Feature',
                    'geometry': json.loads(j.geometry.geojson)
                }
                rasterize(obj, image, fill=0, default_value=180, res=(0.001,), driver='PNG')

                # Remove all .aux.xml files
                os.unlink(image_aux)


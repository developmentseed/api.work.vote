# Work the Elections API

This is the API for the Work the Elections project. The project is sponsored by the Knight Foundation is developed by the Development Seed and [FELN](http://fairelectionsnetwork.com/)

### Local Installation

#### Dependencies

- Python 2.7.10
- Postgres 9.4 with PostGIS support

#### Steps

Install dependencies:

    $ pip install -r requirements

Setup database:

    $ python manage.py migrate
    $ python manage.py createsuperuser

Launch:

    $ python manage.py runserver

### Deployment

`master` branch is deployed to Heroku. To deploy, PR to `master`. Direct push to master is disabled.

### Adding boundaries

Replace the geojson file at `apps/jurisdiction/voteworker.geojson`, then run:

    $ python manage.py boundaries

To generate jurisdiction png files run:

    $ python manage.py rasterize

PNG files are stored at `config/static/jurisdictions`

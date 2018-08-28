FROM python:3.6.3-jessie

EXPOSE 80
EXPOSE 443

RUN apt-get update -y && \
    apt-get install --auto-remove -y \
      libmemcached-dev \
      zlib1g-dev \
      mdbtools \
      vim \
      binutils \
      libproj-dev \
      gdal-bin \
      postgis \
      curl \
      locales \
      apt-transport-https && \
    rm -rf /var/lib/apt/lists/*

RUN echo 'en_US.UTF-8 UTF-8' >> /etc/locale.gen && /usr/sbin/locale-gen

ENV HOME=/home/fec
WORKDIR $HOME

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
RUN pip install rasterio

COPY ./ $HOME/api/
WORKDIR $HOME/api/

ENTRYPOINT ["./bin/entrypoint.sh"]
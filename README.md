# Work the Elections API

This is the API for the Work the Elections project. The project is sponsored by the Knight Foundation is developed by the Development Seed and [FELN](http://fairelectionsnetwork.com/)

## Local Installation

### Dev Dependencies

- Python 3.6.3 
- Postgres 9.6 with PostGIS support
- docker

### Setup Docker Environment

Build the docker image:

     $ docker-compose build base

### Populate the db from a backup

Make sure the db container is stopped:

     $ docker-compose stop db
    
Delete the database files

     $ rm -rf .tmp

Put your backup file in the root folder and rename to `backup.sql`, then run

     $ docker-compose run --rm restore

### Prepare the database

     $ docker-compose run --rm migrate

### Create Super User

     $ docker-compose run --rm createsuperuser

### Serve the API

     $ docker-compose run --rm --service-ports serve

### Adding boundaries

Replace the geojson file at `apps/jurisdiction/voteworker.geojson`, then run:

     $ docker-compose run --rm boundaries

To generate jurisdiction png files run:

     $ docker-compose run --rm rasterize

PNG files are stored at `config/static/jurisdictions`

### Django shell

To access django shell run

     $ docker-compose run --rm shell

## Deployment

`master` branch is deployed to Heroku. To deploy, PR to `master`. Direct push to master is disabled.

# Work the Elections API

[![CircleCI](https://circleci.com/gh/developmentseed/api.work.vote.svg?style=svg)](https://circleci.com/gh/developmentseed/api.work.vote)

This is the API for the Work the Elections project. The project is sponsored by the Knight Foundation is developed by the Development Seed and [FELN](http://fairelectionsnetwork.com/)

## Local Installation

### Dev Dependencies

- Python 3.6.3 
- Postgres 9.6 with PostGIS support
- docker

## Setup Docker Environment

Build the docker image:

     $ docker-compose build base

## Populate the db from a backup

Download the data first:

     $ git clone https://github.com/developmentseed/data.work.vote.git exports

### Prepare the database

     $ docker-compose run --rm migrate

### Create Super User

     $ docker-compose run --rm createsuperuser

### Run import

     $ docker-compose run --rm import

## Serve the API

     $ docker-compose run --rm --service-ports serve

## Adding boundaries

Replace the geojson file at `apps/jurisdiction/voteworker.geojson`, then run:

     $ docker-compose run --rm boundaries

To generate jurisdiction png files run:

     $ docker-compose run --rm rasterize

PNG files are stored at `config/static/jurisdictions`

## Django shell

To access django shell run

     $ docker-compose run --rm shell

## Serve Production

**WARNING:** this is NOT recommended and could damage the production website.

To serve the website with the Heroku environment locally, first download all the environment variables:

     $ heroku config -s -a workelections > config.txt

Then run:

     $ docker-compose run --rm --service-ports prod

## Exporting data

     $ docker-compose run --rm export

## Testing

Run all tests:
     $ docker-compose run --rm base_django_setup python3 manage.py test apps

Run tests, reusing test DB.  This is significantly faster, but requires that tests clean up after themselves.  Django TestCases mostly take care of this.
     $ docker-compose run --rm base_django_setup python3 manage.py test apps --keepdb

## Deployment

`master` branch is deployed to Heroku. To deploy, PR to `master`. Direct push to master is disabled.

### Manual Deployment

We use [Heroku Containers](https://blog.heroku.com/container-registry-and-runtime) for deploying this application to Heroku.

To get started, make sure you are logged in by running `heroku container:login`.

#### Build and Push

     $ heroku container:push web

#### Release

     $ heroku container:release web

#### Migrations

     $ heroku run python manage.py migrate

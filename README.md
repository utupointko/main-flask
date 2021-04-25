# main-flask

## Instructions

### Running

`docker-compose up`

### Migrating

Get into shell of docker container with:

`docker-compose exec backand sh`

Then run

`python manager.py db init`

`python manager.py db migrate`

`python manager.py db upgrade`

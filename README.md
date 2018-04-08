# Robotics Playground Website
This is the new website for Robotics Playground, it is a Django based project

## Directory structure

- `website`: Contains the Django installation

## Development

Install the following:
- Docker

To run the project:

```bash
docker-compose up
```

Django will be hosted on `localhost:8000`.

> NOTE: Windows 10 users might need set the ALLOWED_HOSTS setting within
> Django, see
> [here](https://docs.djangoproject.com/en/1.11/ref/settings/#allowed-hosts)

## Docker Compose commands

Start the dev environment
```bash
docker-compose up -d
```

Stop the dev environment
```bash
docker-compose down
```

Delete the dev environment, including the database
```bash
docker-compose down --volumes
```

Shelling into a container
```bash
docker container ls

docker exec -i -t  #container_id /bin/bash
```

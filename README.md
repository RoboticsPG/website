# Robotics Playground Website
This is the new website for Robotics Playground, it is a Django based project

## Directory structure

- `website`: Contains the Django installation

## Development

Install the following:
- Docker

To run the project:

```bash
./scripts/start.sh
```

Django will be hosted on `localhost:8000`.

> NOTE: Windows 10 users might need set the ALLOWED_HOSTS setting within
> Django, see
> [here](https://docs.djangoproject.com/en/1.11/ref/settings/#allowed-hosts)

## Commands

Start the dev environment
```bash
./scripts/start.sh
```

Stops the dev environment
```bash
./scripts/stop.sh
```

Starts a bash shell
```bash
./scripts/shell.sh
```

Updating (After the Docker config changes)
```bash
./scripts/rebuild.sh
```

Runs the unit tests
```bash
./scripts/run_tests.sh
```

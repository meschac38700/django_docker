# Docker + Django + Postgresql

## Run with Docker

### Quick start with docker compose

```bash
docker-compose up
```

### Running dockerfile image

Using host local database.
`--net=host` to bind locahost to the host machine

```bash
docker run --name {container_name} --rm -ti  --net=host {image_name}
```

# car-plate-database

[toc]

My backend car plate database project with Django, Django REST framework, Celery framework, and Rabbit MQ in docker.

  

## Running in docker environment



### Prerequisites

The image has been tested with the latest images of rabbitmq and postgres.



### Build-up

1. `cd` into the directory.

2. Run the build command:

   ```bash
   docker-compose up --build --force-recreate
   ```

When building, celery will throw ~5x `[Errno 111] Connection refused` before rabbitmq boots up and the connection is established.



**Note:** refrain from explicitly mapping ports for rabbitmq in `docker-compose.yml` as it triggers a docker-compose bug and prevents image from building.



### Container bash commands

- To have full functionality you need to first migrate settings:

```bash
$ docker exec -it src_web_1 bash
$ python manage.py migrate
```

- Create an admin user to have access to the admin panel in `./admin` for an overview of users/database:

```bash
$ docker exec -it src_web_1 bash
$ python manage.py createsuperuser
```



### Accessing database

After the settings have been migrated and admin user has been created, database can be accessed as follows:



#### General database landing page

```
http://localhost:8000/plates/
```

#### Admin panel

```
http://localhost:8000/admin
```

#### API (List)

Return full list of entries in the database

```
http://localhost:8000/api/plates/
```

#### API (Entry by ID)

Replace `<id>` with and id of the entry

```
http://localhost:8000/api/plates/<id>/
```


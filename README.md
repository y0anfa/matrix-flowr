# Matrix Flowr

A small platform to manage your network flows matrices

## Setup (development only !)

1. Run the `docker-compose.yml` in the db directory to setup postgres

```
cd db
docker-compose up -d
```

2. Create a Django superuser

```
cd matrixflowr
python manage.py createsuperuser
```

3. Start the server

```
python manage.py runserver
```

## License

This software is distributed under the MIT license.

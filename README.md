# Observatório 👁‍🗨🎲

## Description 📜

This project is an implementation of my undergraduate thesis.
Which consists in visualize a large number of data in an easier way, through graphs.

## Open Data 🔓

The data analysed comes from a huge CSV file provided by [Brazilian Open Data Portal](http://www.dados.gov.br). This data went through an ETL proccess, by [Leonardo Gabriel Lubczyk](https://github.com/kyrosx/observatorio_etl), to be structured in the database.

## Technologies 🧰

  - [Python](https://docs.python.org/3/)
  - [MySql](https://dev.mysql.com/doc/)
  - [Django Framework](https://docs.djangoproject.com/en/3.0/topics/serialization/)
  - [Django Rest Framework](https://www.django-rest-framework.org)

## Database Structure 🧱
![image-model-v2](https://user-images.githubusercontent.com/29782248/86071500-c77bfe80-ba55-11ea-83ab-9a866de168e1.png)

## First Steps 🧭

**Windows**

- Make sure you already have installed pip:
``` shell
> pip --version
```

- Install Pipenv environment package manager:
``` shell
> pip install pipenv
```

- Activate environment:
``` shell
> pipenv shell
```

- Check requirements:
``` shell
> pipenv check
```

- Install all project dependencies:
``` shell
> pipenv install
> pipenv install --dev
```

- Alter databases config to your `NAME`, `USER` and `PASSWORD` in `core/settings.py`, like:
``` python
NAME = 'observatorio'
USER = 'root'
PASSWORD = ''
```

- Create the database `NAME` in your server:
``` sql
CREATE DATABASE observatorio DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_as_ci;
```

- Run migrations:
``` shell
> py manage.py migrate
```

- Run server:
``` shell
> py manage.py runserver
```

## URLS

**Data**

- All data:
``` browser
localhost:8000/chart/data
```

- Filtered data:
```
localhost:8000/chart/data/?information_nickname=&location_name=&granularity=&in_date_gt=&until_date_lte=
```

- Dates format:
```
YYYY-MM-DD
```

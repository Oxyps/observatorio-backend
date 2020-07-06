# Observatório 👁‍🗨🎲

## Status: *in development* ⏳

## Description 📜
This project is an implementation of my undergraduate thesis.
Which consists in visualize a large number of data in an easier way, through charts.

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
CREATE DATABASE observatorio DEFAULT CHARACTER SET utf8mb4;
```

- Run migrations:
``` shell
> py manage.py migrate
```

- Run `scripts/populate_outer_tables.sql` in DB to populate tables around `chart_data` table; It can easily be done using [MySQL-Workbench](https://dev.mysql.com/downloads/workbench/); Make sure to assegurate the UTF-8 unicode;

- **in development:**
Run `scripts/code/generate_insert_script.py` to generate `scripts/populate_data_table.sql`;

- **in development:**
Run `scripts/populate_data_table.sql` in DB to populate `Data` table;

- With DB populated, a JSON file must be extracted from `Data` table using `scripts/data_source/extraction_query.sql` extraction query. This file must be named `data.json` and be in the same script's directory. This procedure can also be done using [MySQL-Workbench](https://dev.mysql.com/downloads/workbench/);

- Then, with all data in `scripts/data_source/data.json` created, run `scripts/code/generate_jsons.py` to generate the 6298 location JSON files;

- Now the API is ready to be consumed; run server:
``` shell
> py manage.py runserver
```

## URLS 📁

**Data**
- Fetch informations:
```
localhost:8000/chart/information
```

- Fetch granularities:
```
localhost:8000/chart/granularity
```

- Filtered data:
```
localhost:8000/chart/data/?information_nickname=&location_name=&location_type=&granularity=&in_date_gt=&until_date_lte=
```

**Util**
- Dates format: `yyyy-mm-dd`

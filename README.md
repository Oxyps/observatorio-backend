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

- Run `scripts/populate_outer_tables.sql` in DB to populate tables around `Data` table; It can easily be done using [ApexSQL extension for VSCode](https://www.sqlshack.com/visual-studio-code-for-mysql-and-mariadb-development/); Assegurate the UTF-8 unicode;

- Run `util/scripts/populate_data_table.sql` in DB to populate `Data` table;

- After DB populated, a JSON file must be extracted from `Data` table using `util/scripts/extraction_query.sql` extraction query. This file must be named `util/data_source/data.json` and be in the same script's directory. That procedure can also be done using [ApexSQL extension for VSCode](https://solutioncenter.apexsql.com/how-to-export-mysql-data-to-json/);

- Run server:
``` shell
> py manage.py runserver
```

- Request to `localhost:8000/chart/generate-json-locations` to generate the locations JSON files which will be used for searches; This route should be used only once;

- Now API is ready to be consumed.

## URLS 📁

**Data**
- Fetch informations:
```
localhost:8000/chart/information/
```

- Fetch granularities:
```
localhost:8000/chart/granularity/
```

- Fetch locations:
```
localhost:8000/chart/location/
```

- Filtered data:
```
http://localhost:8000/chart/search-data/?information_nickname=FUNDEB&location_name=Acrelândia&location_type=Município&location_state=AC&granularity=bimonthly&in_date_gt=2007-01-01&until_date_lte=2019-12-31
```

- **This route later will need some kind of authentication.** Generate locations JSON files:
```
localhost:8000/chart/generate-json-files/
```

**Util**
- Dates format: `yyyy-mm-dd`

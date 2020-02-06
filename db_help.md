# Database Help

## Migrate Commands

python3 manage.py db init
python3 manage.py db migrate -m ""
python3 manage.py db upgrade

## Errors

ERROR [root] Error: Target database is not up to date.

```os
python3 manage.py db stamp head
```

## PSQL Commands

CREATE TABLE
DROP TABLE

quit

```psql
\q
```

list
databases
tables

```psql
\l
\dt
```

## Heroku

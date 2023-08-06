# Dataframe to Database

![Build](https://github.com/proafxin/df_to_db/actions/workflows/build.yml/badge.svg)

![codecov](https://github.com/proafxin/df_to_db/blob/develop/coverage.svg)

Write a pandas dataframe to a database directly. The `df.to_sql` is severely insufficient for this purpose. It not only overwrites the current table, it also requires manually creating an `SQLAlchemy` engine for connection. `df-to-db` is meant to take all the extra steps away from this writing process. Currently, the goal is to support both SQL and NoSQL databases including data warehouse such as `Google BigQuery` or `Apache Cassandra` (they are not supported at the moment). For SQL databases, `SQLAlchemy` is used internally for generalizing all SQL database connections.

## Supported So Far

* MySQL
* Postgresql
* SQL Server
* Mongo
* Google BigQuery

## Notes for Linux

You may need some packages otherwise `mysqlclient` installation may fail. Command for installing these in Debian/Ubuntu: `sudo apt-get install python3-dev default-libmysqlclient-dev build-essential`.

## Environment setup

Create a virtual environment and activate it. Inside the virtual environment, run `pip install -r requirements.txt`. If you get this error `git clone --filter=blob:none --quiet 'ssh://****@github.com/proafxin/df_to_db.git' '..\df_to_db\env\src\dataframe-to-database' did not run successfully`, then go to `requirements.txt` and remove the line `-e git+ssh://git@github.com/proafxin/df_to_db.git...`. Now the command should run succesfully. If you are on windows and get the following error `tests run-test: commands[0] | python3 calculate_coverage.py WARNING: test command found but not installed in testenv`, then replace `python3 calculate_coverage.py` by `python calculate_coverage.py` or make `python3` available in tox.

## Example Usage

## Writing to SQL Database

For SQL databases, use `SQLDatabaseWriter`.

```python
from write_df.sql_writer import SQLDatabaseWriter

writer = SQLDatabaseWriter(
    dbtype="mysql",
    host=MYSQL_HOST,
    dbname=DBNAME,
    user=MYSQL_USER,
    password=MYSQL_PASSWORD,
    port=MYSQL_PORT,
)
```

`dbtype` can be one of the SQL databses supported i.e. one of `mysql, postgresql, sqlserver`.
Get the list of databases using the connection.

```python
database_names = writer.get_list_of_database()
```

Check if the database has a certain table `table_name`.

```python
writer.has_table(table_name=table_name)
```

Write the dataframe to the database using this connection.

```python
result = writer.write_df_to_db(
    data=data,
    table_name=table_name,
    id_col=None,
    drop_first=True,
)
```

`data` is the actual dataframe to write. This `result` is an SQLAlchemy `CursorResult` object. `id_col` is the column name of the primary key (corresponding to `id` column of a table). If this column exists in the dataframe itself, pass the name of the column in this argument. If `drop_first` is `True`, then the table will be dropped and created from the dataframe schema. Otherwise, the writer will read the schema from the database, check whether there is any null data in non-nullable columns and then try to write the data to the table. Needless to say, the column names must be identical in dataframe and the table.

## Writing to NoSQL Database

Create the writer object.

```python
from write_df.nosql_writer import NoSQLDatabaseWriter

writer = NoSQLDatabaseWriter(
    dbtype="mongo",
    host=os.environ["MONGO_HOST"],
    dbname=DBNAME,
    user=os.environ["MONGO_USER"],
    password=os.environ["MONGO_PASSWORD"],
    port=int(os.environ["MONGO_PORT"]),
)
```

Get list of databases.

```python
dbnames = writer.get_list_of_databases()
```

Get list of collections of the current database.

```python
collection_names = writer.get_list_of_collections()
```

Get a certain collection or create it.

```python
collection = writer.get_or_create_collection(collection_name=collection_name)
```

Get document count of a collection.

```python
doc_count = writer.get_document_count(collection_name=collection_name)
```

Write to a collection `collection_name`.

```python
result = write_data_to_collection(collection_name=collection_name, data=data)
```

## Writing to Google BigQuery Tables

Create a writer object.

```python
writer = BigQueryWriter(
    path_to_credentials=os.environ["GOOGLE_APPLICATION_CREDENTIALS"],
)
```

Here, ```path_to_credentials``` is the path to the json file that contains Gooogle service account information. It should contain fields like `project_id`, `private_key`, `client_id`, etc.

You can get a certain dataset within the default project.

```python
datset = writer.get_dataset(dataset_id=os.environ["BIGQUERY_DATASET"])
```

Get the table reference and table object directly using:

```python
table_ref = writer.get_table_ref(dataset_id=dataset_id, table_name=table_name)

table = get_table(dataset_id=dataset_id, table_name=table_name)
```

If you want to empty a table:

```python
writer.delete_all_rows(dataset_id=dataset_id, table_name=table_name)
```

Finally, write to a table:

```python
writer.write_to_table(
    data=data,
    dataset_id=dataset_id,
    table_name=table_name,
)
```

Here, `data` is the pandas dataframe that is to be written to the table. If the table does not have any schema, then it is assumed that it is an empty table. Otherwise, schema is available and the rows from the dataframe are simply appended to the existing table.

## Generate Documentation Source Files

You should not have to do this but in case you want to generate the source ReStructuredText files yourself, here is how. Skip to the next section to simply generate html documentation locally.

Change to docs directory `cd docs/`. Run `sphinx-quickstart`. Choose `y` when it asks to seperate build and source directories.

Change to `docs/source` directory. In `conf.py`, add the following lines at the start of the script.

```python
import os
import sys

sys.path.insert(0, os.path.abspath("../.."))
```

and save it. Add `"sphinx.ext.autodoc",` to the `extensions` list. Run `python -m pip install -U sphinx_rtd_theme` and set `html_theme = "sphinx_rtd_theme"` (or whatever theme you want).

In `index.rst`, add `modules` to toctree. The structure should look like this:

```markdown
.. toctree::
:maxdepth: 2
:caption: Contents:

modules
```

Run `sphinx-apidoc -f -o . ../../ ../../calculate_coverage.py  ../../setup.py ../../tests/`. It should generate the necessary ReStructuredText files for documentation.

## Generating HTML Documentation

Change to `docs/` using `cd ..` then run `.\make clean` and `.\make html`. Output should be built with no errors or warnings. You will get the html documenation in `docs/build/html` directory. Open `index.html`.

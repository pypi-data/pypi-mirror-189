# Trail db

A small demo library to save mlflow run data to a mongodb.

# Installation
'''
pip install traildb
'''
# Get started

'''
from traildb import DB_import

# Instantiate a DB_import object
db_imp = DB_import(URI, database_name)

# Call the add_db method
result = db_imp.add_db(data)
'''
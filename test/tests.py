import os
import config
from controller import logger
from db import Database

# Change this to a table on the database
test_table = 'test_table'

def test_log():
    return os.path.exists(config.log['file'])

def test_sqlalchemy():
    ''' Checks if sqlalchemy can be imported and logs version'''
    try:
        import sqlalchemy
    except Exception as e:
        logger.error("Import error: %s", e)
        return False
    else:
        from sqlalchemy import create_engine
        version = sqlalchemy.__version__
        logger.info("Sqlalchemy version: %s", version)
        return True

def test_sql_connection():
    database = Database(config,logger)
    result = [False, False, False]
    try:
        engine = database.database_engine()
        if engine == None:
            return result
        result[0] = True
        connection = database.database_connect(engine)
        if connection == None:
            return result
        result[1] = True
        table = database.reflect_table(test_table, terminate=True, connection=connection)
        if table == None:
            return result
        result[2] = True
        logger.info(table.columns)
        logger.info(table.primary_key)
        database.database_disconnect(connection)
        engine.dispose()

    except Exception as e:
        logger.error("Unexpected exception on test: %s", e)

    return result

def run_tests():
    ''' Run tests and returns a dictionary with results '''
    log_result = test_log()
    connection_result = False
    sqlalchemy_result = test_sqlalchemy()

    if sqlalchemy_result:
        sql_result = test_sql_connection()

    return {'logger': log_result,
            'sqlalchemy': sqlalchemy_result,
            'engine': sql_result[0],
            'connection': sql_result[1],
            'reflect_table': sql_result[2]
            }

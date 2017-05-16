import os
import config
from controller import logger
from db import Database


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
    try:
        engine = database.database_engine()
        connection = database.database_connection(engine)
        return database.database_disconnect(connection) == None
    except Exception as e:
        logger.error("Unexpected exception: %s", e)
        return False

def run_tests():
    ''' Run tests and returns a dictionary with results '''
    log_result = test_log()
    connection_result = False
    sqlalchemy_result = test_sqlalchemy()

    if sqlalchemy_result:
        connection_result = test_sql_connection()

    return {'logger': log_result,
            'sqlalchemy': sqlalchemy_result,
            'connection': connection_result
            }

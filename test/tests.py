import os
import config
from controller import logger
from database import test_sqlalchemy, test_sql_connection


def test_log():
    return os.path.exists(config.log['file'])

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

import os
import config
from controller import logger


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
    ''' Attempts to create a test table and do an insert and select.'''
    from sqlalchemy import create_engine, Table, Column, Integer, MetaData, String
    logger.info('Testing sqlalchemy connection')
    engine = create_engine('sqlite:///:memory:', echo=False)
    metadata = MetaData()

    # creating connection
    conn = engine.connect()
    if not conn:
        logger.error("Could not connect to database")
        return False
    logger.info('Created connection')

    # test table
    test = Table('tests', metadata,
                 Column('test_id', Integer(), primary_key=True),
                 Column('test_string', String(50), index=True),
                 )
    # creating table
    test.create(engine)
    logger.info('Created memory-only table')
    conn.execute(test.insert().values(test_id=1, test_string='test'))
    result = [row for row in conn.execute(test.select())]
    return result > 0


def run_tests():
    ''' Run tests and returns a dictionary with results '''
    log_result = test_log()
    sqlalchemy_result = test_sqlalchemy()
    connection_result = False
    if sqlalchemy_result:
        connection_result = test_sql_connection()

    return {'logger': log_result,
            'sqlalchemy': sqlalchemy_result,
            'connection': connection_result
            }

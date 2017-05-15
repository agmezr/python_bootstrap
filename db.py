from sqlalchemy import exc, create_engine, MetaData, Table
from controller import decode
import logging

class Database:

    def __init__(self, config, log=None):
        self.config = config
        if not log:
            log = logging
        self.log = log

    def database_engine(self):
        ''' Create a database connection engine '''
        engine = None
        try:
            config = self.config

            user = config.database.get('username', None)
            password = decode(config.database.get('password', None))
            host = config.database.get('host', 'localhost')
            port = config.database.get('port', 1234)
            database = config.database.get('database', None)
            dbms = config.database.get('dbms', None)

            if not user or not password or not database or not dbms:
                self.log.warn('Failed to define SQL URI, there are missing parameters in your configuration')
                return engine
            sql_uri = '{dbms}://{user}:{password}@{host}:{port}/{database}'.format(
                dbms=dbms,
                user=user,
                password=password,
                host=host,
                port=port,
                database=database
            )
            pool_size = config.database.get('pool_size', None)
            max_overflow = config.database.get('max_overflow', 0)
            pool_recycle = config.database.get('pool_recycle', None)
            isolation_level = config.database.get('isolation_level', 'READ UNCOMMITED')
            engine = create_engine(sql_uri, echo=False)
            if pool_size is not None and pool_recycle is not None:
                self.log.info('Setting pool configuration')
                engine.pool_size = pool_size
                engine.max_overflow = max_overflow
                engine.pool_recycle = pool_recycle

            self.log.info('Setting isolation level')
            engine.isolation_level = isolation_level

        except exc.SQLAlchemyError as error:
            self.log.error('Failed to create an engine: {e}'.format(e=error))
        except Exception as error:
            self.log.error('Unexpected exception: {e}'.format(e=error))
        else:
            self.log.info('Engine created')
        finally:
            return engine

    def database_connection(self, engine=None):
        '''Start a connection to the database'''
        connection = None
        try:
            if not engine:
                engine = self.engine()
            connection = engine.connect()
        except exc.SQLAlchemyError as error:
            self.log.error('Failed to start connection: {e}'.format(e=error))
        except Exception as error:
            self.log.error('Unexpected exception: {e}'.format(e=error))
        else:
            self.log.info('Connection to database created')
        finally:
            return connection

    def reflect_table(self, tablename, connection=None):
        ''' Reflect a table '''
        table = None
        if not connection:
            connection = self.database_connection()
        if connection and tablename: 
            try:
                meta = MetaData()
                meta.reflect(bind=connection)
                table = Table(
                    tablename,
                    meta,
                    autoload=True,
                    autoload_with=connection
                )
            except exc.SQLAlchemyError as error:
                self.log('Failed to reflect table: {e}'.format(e=error))
            except Exception as error:
                self.log('Unexpected exception: {e}'.format(e=error))
        else:
            self.log('Could not initiate connection using the engine')
        return table

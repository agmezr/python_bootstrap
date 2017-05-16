# log settings
log = {
    'file': './log/app.log',
    'format': '%(levelname) -5s %(asctime)s %(message)s',
    'keep': 5,
    'level': 'debug',
    'limit': 1000000
    }

# database configuration, change this if you plan to use sqlalchemy
database = {
    'user': '<USERNAME>',
    'password': '<PASSWORD>',
    'dbms':'<DBMS>',
    'database':'<DATABASE>',
    'host': 'localhost',
    'port': 1234,
    'pool_size': 5,
    'max_overflow': 0,
    'pool_recycle': 2,
    'isolation_level': 'READ_UNCOMMITED'
}

app = {
    'key': 'mysecretkey1234'
}

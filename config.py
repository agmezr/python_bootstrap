# log settings
log = {
    'file': './log/app.log',
    'format': '%(levelname) -5s %(asctime)s %(message)s',
    'keep': 5,
    'level': 'debug',
    'limit': 1000000
    }

# database configuration
database = {
    'username': '<USERNAME>',
    'password': '<PASSWORD>',
    'host': 'localhost',
    'port': 1234,
    'database':'<DATABASE>',
    'dbms':'<DBMS>'
}

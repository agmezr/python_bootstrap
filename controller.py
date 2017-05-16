from logging import getLogger, handlers, Formatter
from simplecrypt import decrypt, encrypt
from base64 import b64decode, b64encode
import config

logger = getLogger('app')
handler = handlers.RotatingFileHandler(
    config.log.get('file', './app.log'),
    maxBytes=config.log.get('limit', 10000),
    backupCount=config.log.get('keep', 1)
)

log_format = config.log.get('format', None)
if log_format:
    handler.setFormatter(Formatter(log_format))
logger.setLevel(config.log.get('level', 'info').upper())
logger.addHandler(handler)

def decode(value, key):
    if value and key:
        value = decrypt(key, b64decode(value))
    return value

def encode(value, key):
    if value:
        return b64encode(encrypt(key,value))

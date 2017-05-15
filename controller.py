import logging
import config
from logging.handlers import RotatingFileHandler

logger = logging.getLogger('app')
handler = RotatingFileHandler(config.log.get('file', './app.log'),
                              maxBytes=config.log.get('limit', 10000),
                              backupCount=config.log.get('keep', 1))

log_format = config.log.get('format', None)
if log_format:
    handler.setFormatter(logging.Formatter(log_format))
logger.setLevel(config.log.get('level', 'info').upper())
logger.addHandler(handler)

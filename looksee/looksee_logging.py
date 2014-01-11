import logging

from redislog import handlers, logger

from tasa.store import connection

logging.setLoggerClass(logger.RedisLogger)

# this is probably not ideal, but it works for now
logging.basicConfig(level=logging.INFO)

# Modify the root logger to use this handler
log = logging.getLogger()
log.addHandler(handlers.RedisHandler('logging', connection,
                                     level=logging.INFO))

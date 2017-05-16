from controller import logger, encode
from test import tests
import config

logger.info("Starting test")
results = tests.run_tests()

print "Results for tests"

row_format ="{:>15}" * 2
for r, row in [(result, results[result] and "OK" or "Error" ) for result in results]:
    logger.info("Result for %s: %s", r,row)
    print row_format.format(r, row)


#print encode('root',config.app['key'])

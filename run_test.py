from controller import logger
from test import tests

logger.info("Starting test")
results = tests.run_tests()

print "Results for tests"

row_format ="{:>10}" * 2
for r, row in [(result, results[result] and "OK" or "Error" ) for result in results]:
    print row_format.format(r, row)

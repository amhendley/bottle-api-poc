import unittest
import xmlrunner


loader = unittest.TestLoader()
tests = loader.discover(start_dir='tests')

with open('./test-results.xml', 'wb') as output:
    runner = xmlrunner.XMLTestRunner(output)
    runner.failfast = False
    runner.buffer = False
    runner.verbosity = 2

    runner.run(test=tests)

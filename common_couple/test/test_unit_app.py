import unittest
import xmlrunner
import os
import logging as log

from test_most_common_couple import TestMostCommonCouple


def add_tests_to_suite():

    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestMostCommonCouple))
    return suite


if __name__ == "__main__":

    try:
        test_report_path = os.path.join("test-report")

        runner = unittest.TextTestRunner()
        xmlrunner.XMLTestRunner(output=test_report_path).run(add_tests_to_suite())
    except Exception as e:
        log.error(f"failed to running Unit Tests with error: {e}")

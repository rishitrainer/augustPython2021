import unittest
from learn_day016.ValidationTestCases import TestValidations
from learn_day016.TestAnotherValidations import TestAnotherCases

def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestValidations('test_validate_age_positive'))
    suite.addTest(TestValidations('test_validate_age_negative'))
    suite.addTest(TestValidations('test_validate_age_Boundary'))
    suite.addTest(TestAnotherCases('test_validate_age_InvalidAge'))
    return suite


test_cases = (TestValidations, TestAnotherCases)
def loader_suite():
    suite = unittest.TestSuite()
    for each_testcase in test_cases:
        tests = unittest.TestLoader().loadTestsFromTestCase(each_testcase)
        suite.addTests(tests)
    return suite


runner = unittest.TextTestRunner()
runner.run(loader_suite())

import unittest
from learn_day016.AgeValidation import validate_age, InvalidAgeError

class TestValidations(unittest.TestCase):
    '''
      1.  test_validate_age_0, validate_age_1
      2. test_validate_age_positive
      3. test_validate_age_20
    '''
    def setUp(self):
        print("Executed before test case")

    def tearDown(self):
        print("Executed After test Case")

    @staticmethod
    def setUpClass() -> None:
        print("Executed once when class instantiate")

    @staticmethod
    def tearDownClass() -> None:
        print("Executed once when class destroys")

    def test_validate_age_positive(self):
        print("test_validate_age_positive")
        actual = validate_age(20)
        self.assertEqual(True, actual) # comparison with expected
        self.assertTrue(actual) # true or not

    def test_validate_age_negative(self):
        print("test_validate_age_negative")
        actual = validate_age(8)
        self.assertEqual(False, actual) # comparison with expected
        self.assertFalse(actual) # False or not

    def test_validate_age_Boundary(self):
        print("test_validate_age_Boundary")
        actual = validate_age(18)
        self.assertEqual(True, actual) # comparison with expected
        self.assertTrue(actual) # True or not



# 4. range - 0 - 121 -
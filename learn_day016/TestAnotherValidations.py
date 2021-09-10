import unittest
from learn_day016.AgeValidation import validate_age, InvalidAgeError

class TestAnotherCases(unittest.TestCase):

    def test_validate_age_InvalidAge(self):
        with self.assertRaises(InvalidAgeError):
            validate_age("ABC")
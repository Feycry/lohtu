import unittest
from util import validate_reference, UserInputError

class TestReferenceValidation(unittest.TestCase):
    def setUp(self):
        pass

    def test_valid_length_does_not_raise_error(self):
        validate_reference("juokse")
        validate_reference("a" * 100)

    def test_too_short_or_long_raises_error(self):
        with self.assertRaises(UserInputError):
            validate_reference("ole")

        with self.assertRaises(UserInputError):
            validate_reference("koodaa" * 20)

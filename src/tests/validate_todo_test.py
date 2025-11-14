import unittest
from util import validate_todo, UserInputError

class TestTodoValidation(unittest.TestCase):
    def setUp(self):
        pass

    def test_valid_length_does_not_raise_error(self):
        validate_todo("juokse")
        validate_todo("a" * 100)

    def test_too_short_or_long_raises_error(self):
        with self.assertRaises(UserInputError):
            validate_todo("ole")

        with self.assertRaises(UserInputError):
            validate_todo("koodaa" * 20)

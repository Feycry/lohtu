import unittest
from util import validate_reference, UserInputError

class TestReferenceValidation(unittest.TestCase):
    def test_valid_min_boundary(self):
        validate_reference("ab")

    def test_valid_max_boundary(self):
        validate_reference("a" * 100)

    def test_basic_valid(self):
        validate_reference("abc")

    def test_too_short_empty(self):
        with self.assertRaises(UserInputError):
            validate_reference("")

    def test_too_short_single_char(self):
        with self.assertRaises(UserInputError):
            validate_reference("a")

    def test_too_long(self):
        with self.assertRaises(UserInputError):
            validate_reference("a" * 101)

    def test_unicode_characters(self):
        validate_reference("ÄäÖöß你好")

    def test_special_characters(self):
        validate_reference("Title: @ref_type #1 (v2.0)")

    def test_none_raises_type_error(self):
        with self.assertRaises(TypeError):
            validate_reference(None)

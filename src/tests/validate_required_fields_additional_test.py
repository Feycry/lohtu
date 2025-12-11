import unittest
from util import validate_required_fields, UserInputError


class TestValidateRequiredFieldsAdditional(unittest.TestCase):
    def test_positive_cases_for_multiple_types(self):
        validate_required_fields("booklet", {"title": "T"})
        validate_required_fields("manual", {"title": "T"})
        validate_required_fields("misc", {})
        validate_required_fields("proceedings", {"title": "T", "year": "2024"})
        validate_required_fields("unpublished", {"author": "A", "title": "T"})

    def test_missing_required_fields_for_types(self):
        with self.assertRaises(UserInputError):
            validate_required_fields("conference", {"author": "A", "title": "T"})
        with self.assertRaises(UserInputError):
            validate_required_fields("inbook", {"author": "A", "title": "T", "publisher": "P"})
        with self.assertRaises(UserInputError):
            validate_required_fields("incollection", {"author": "A", "title": "T", "publisher": "P"})
        with self.assertRaises(UserInputError):
            validate_required_fields("phdthesis", {"author": "A", "title": "T", "year": "2024"})
        with self.assertRaises(UserInputError):
            validate_required_fields("techreport", {"author": "A", "title": "T", "year": "2024"})

    def test_whitespace_only_fields_fail(self):
        with self.assertRaises(UserInputError):
            validate_required_fields("unpublished", {"author": " ", "title": "T"})
        with self.assertRaises(UserInputError):
            validate_required_fields("proceedings", {"title": " ", "year": "2020"})

    def test_unknown_type_has_no_requirements(self):
        validate_required_fields("unknown_kind", {"author": "A"})

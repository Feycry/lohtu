import unittest
from util import validate_reference, UserInputError
from util import validate_required_fields

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

    # Required field validations for different types
    def test_inproceedings_missing_author(self):
        with self.assertRaises(UserInputError) as cm:
            validate_required_fields("inproceedings", {
                "title": "T",
                "booktitle": "B",
                "year": "2024",
            })
        self.assertIn("Author is required", str(cm.exception))

    def test_inproceedings_missing_booktitle(self):
        with self.assertRaises(UserInputError) as cm:
            validate_required_fields("inproceedings", {
                "author": "A",
                "title": "T",
                "year": "2024",
            })
        self.assertIn("Booktitle is required", str(cm.exception))

    def test_article_missing_journal(self):
        with self.assertRaises(UserInputError) as cm:
            validate_required_fields("article", {
                "author": "A",
                "title": "T",
                "year": "2024",
            })
        self.assertIn("Journal is required", str(cm.exception))

    def test_book_missing_publisher(self):
        with self.assertRaises(UserInputError) as cm:
            validate_required_fields("book", {
                "author": "A",
                "title": "T",
                "year": "2022",
            })
        self.assertIn("Publisher is required", str(cm.exception))

    def test_mastersthesis_missing_school(self):
        with self.assertRaises(UserInputError) as cm:
            validate_required_fields("mastersthesis", {
                "author": "A",
                "title": "T",
                "year": "2021",
            })
        self.assertIn("School is required", str(cm.exception))

    def test_inproceedings_spaces_only_author(self):
        with self.assertRaises(UserInputError) as cm:
            validate_required_fields("inproceedings", {
                "author": "   ",
                "title": "T",
                "booktitle": "B",
                "year": "2024",
            })
        self.assertIn("Author is required", str(cm.exception))

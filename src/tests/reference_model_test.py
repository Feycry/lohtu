import unittest
from entities.reference import Reference


class TestReferenceModel(unittest.TestCase):
    def test_getitem_existing_and_missing(self):
        ref = Reference(1, author="John", title="T")
        self.assertEqual(ref["author"], "John")
        self.assertIsNone(ref["nonexistent"])

    def test_str_formats_with_type_and_fields(self):
        ref = Reference(
            2,
            ref_type="article",
            author="John Doe",
            title="Sample",
            year="2023",
        )

        text = str(ref)
        self.assertIn("Type: @article", text)
        self.assertTrue(text.startswith("Type: @article"))

        self.assertIn("Author: John Doe", text)
        self.assertIn("Title: Sample", text)
        self.assertIn("Year: 2023", text)

    def test_str_with_no_fields_falls_back_to_id(self):
        ref = Reference(3)
        self.assertEqual(str(ref), "Reference #3")

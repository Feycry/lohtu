import unittest
from entities.reference import Reference


class TestReferenceToBibtex(unittest.TestCase):

    def test_to_bibtex_formats_reference_correctly(self):
        #Arrange
        reference = Reference(
            reference_id=1,
            ref_type="article",
            author="John Doe",
            title="Sample Article Title",
            journal="Test Journal",
            year="2023",
            volume="10",
            pages="123-456"
        )

        expected_bibtex = (
            "@article{1,\n"
            "\tauthor: John Doe,\n"
            "\ttitle: Sample Article Title,\n"
            "\tjournal: Test Journal,\n"
            "\tyear: 2023,\n"
            "\tvolume: 10,\n"
            "\tpages: 123-456\n"
            "}"
        )

        #Act and Assert
        self.assertEqual(reference.to_bibtex(), expected_bibtex)
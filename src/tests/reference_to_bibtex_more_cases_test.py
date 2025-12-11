import unittest
from entities.reference import Reference


class TestReferenceToBibtexMoreCases(unittest.TestCase):
    def test_field_order_follows_ORDERED_KEYS(self):
        ref = Reference(
            10,
            ref_type="inproceedings",
            title="Order Test",
            author="Alpha",
            booktitle="Conf",
            year="2024",
            doi="10.1000/test",
            url="http://example.com",
        )
        bib = ref.to_bibtex()
        # Ensure header first, then author before title, then booktitle, year, url, doi
        self.assertTrue(bib.startswith("@inproceedings{10,"))
        self.assertLess(bib.find("author = {Alpha}"), bib.find("title = {Order Test}"))
        self.assertLess(bib.find("title = {Order Test}"), bib.find("booktitle = {Conf}"))
        self.assertLess(bib.find("booktitle = {Conf}"), bib.find("year = {2024}"))
        self.assertLess(bib.find("year = {2024}"), bib.find("url = {http://example.com}"))
        self.assertLess(bib.find("url = {http://example.com}"), bib.find("doi = {10.1000/test}"))

    def test_special_characters_and_braces(self):
        ref = Reference(
            11,
            ref_type="article",
            author="{John, Doe}",
            title="Sample, {Complex} Title",
            journal="J. Testing",
            year="2023",
        )
        bib = ref.to_bibtex()
        self.assertIn("author = {{John, Doe}}", bib)
        self.assertIn("title = {Sample, {Complex} Title}", bib)

    def test_includes_doi_and_url_when_present(self):
        ref = Reference(
            12,
            ref_type="article",
            author="A",
            title="B",
            journal="J",
            year="2022",
            doi="10.1/abc",
            url="https://ex.com/x",
        )
        bib = ref.to_bibtex()
        self.assertIn("doi = {10.1/abc}", bib)
        self.assertIn("url = {https://ex.com/x}", bib)

    def test_book_type_formatting(self):
        ref = Reference(
            13,
            ref_type="book",
            author="Author",
            title="Book Title",
            publisher="Pub",
            year="2021",
            edition="2",
        )
        bib = ref.to_bibtex()
        self.assertTrue(bib.startswith("@book{13,"))
        self.assertIn("publisher = {Pub}", bib)
        self.assertIn("edition = {2}", bib)

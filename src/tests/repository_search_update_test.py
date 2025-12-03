import unittest
from config import app
from db_helper import reset_db
from repositories.reference_repository import (
    create_reference,
    get_references,
    get_reference,
    update_reference,
    get_reference_type_required_fields,
)


class TestRepositorySearchAndUpdate(unittest.TestCase):
    def setUp(self):
        with app.app_context():
            reset_db()

            create_reference(
                "inproceedings",
                author="Alice",
                title="Graph Algorithms",
                booktitle="AlgoConf",
                year="2024",
            )
            create_reference(
                "article",
                author="Bob",
                title="Data Structures",
                journal="CS Journal",
                year="2023",
            )

    def test_get_references_no_query_returns_all(self):
        with app.app_context():
            refs = get_references()
            self.assertGreaterEqual(len(refs), 2)

            self.assertEqual(refs[0].title, "Data Structures")

    def test_get_references_with_query_filters(self):
        with app.app_context():
            refs = get_references("graph")
            self.assertEqual(len(refs), 1)
            self.assertEqual(refs[0].title, "Graph Algorithms")

    def test_update_reference_persists_changes(self):
        with app.app_context():

            refs = get_references()
            target_id = refs[0].id
            ref_type = refs[0].ref_type
            update_reference(
                reference_id=target_id,
                reference_type=ref_type,
                author=refs[0].author,
                title=refs[0].title,
                booktitle=getattr(refs[0], "booktitle", None),
                year="2025",  # change
                url=getattr(refs[0], "url", None),
                doi=getattr(refs[0], "doi", None),
                editor=getattr(refs[0], "editor", None),
                volume=getattr(refs[0], "volume", None),
                number=getattr(refs[0], "number", None),
                series=getattr(refs[0], "series", None),
                pages=getattr(refs[0], "pages", None),
                address=getattr(refs[0], "address", None),
                month=getattr(refs[0], "month", None),
                organization=getattr(refs[0], "organization", None),
                publisher=getattr(refs[0], "publisher", None),
                edition=getattr(refs[0], "edition", None),
                howpublished=getattr(refs[0], "howpublished", None),
                institution=getattr(refs[0], "institution", None),
                journal=getattr(refs[0], "journal", None),
                note=getattr(refs[0], "note", None),
                school=getattr(refs[0], "school", None),
                type=getattr(refs[0], "type", None),
            )
            updated = get_reference(target_id)
            self.assertIsNotNone(updated)
            self.assertEqual(updated.year, "2025")

    def test_get_reference_type_required_fields(self):
        with app.app_context():
            req = get_reference_type_required_fields("inproceedings")
            self.assertIn("author", req)
            self.assertIn("title", req)
            self.assertIn("booktitle", req)
            self.assertIn("year", req)

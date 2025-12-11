import unittest
from config import app
from db_helper import reset_db, setup_db
from repositories.reference_repository import (
    create_reference,
    get_references,
    get_reference,
    update_reference,
)


class TestRepositoryAdditional(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with app.app_context():
            setup_db()

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

    def test_get_reference_not_found(self):
        with app.app_context():
            ref = get_reference(99999)
            self.assertIsNone(ref)

    def test_filter_by_author_and_journal(self):
        with app.app_context():
            refs = get_references("Bob")
            self.assertEqual(len(refs), 1)
            self.assertEqual(refs[0].author, "Bob")
            refs2 = get_references("CS Journal")
            self.assertEqual(len(refs2), 1)
            self.assertEqual(refs2[0].journal, "CS Journal")

    def test_update_optional_fields_to_none(self):
        with app.app_context():
            refs = get_references()
            target = refs[0]
            update_reference(
                reference_id=target.id,
                reference_type=target.ref_type,
                author=target.author,
                title=target.title,
                booktitle=None,
                year=target.year,
                url=None,
                doi=None,
                editor=None,
                volume=None,
                number=None,
                series=None,
                pages=None,
                address=None,
                month=None,
                organization=None,
                publisher=None,
                edition=None,
                howpublished=None,
                institution=None,
                journal=getattr(target, "journal", None),
                note=None,
                school=None,
                type=None,
            )
            updated = get_reference(target.id)
            self.assertEqual(updated.year, target.year)

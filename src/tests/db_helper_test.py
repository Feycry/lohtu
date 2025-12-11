import unittest
from config import app
from db_helper import setup_db, tables, reset_db, delete_reference
from repositories.reference_repository import create_reference, get_references


class TestDbHelper(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with app.app_context():
            setup_db()

    def test_setup_db_creates_expected_tables(self):
        with app.app_context():
            tbls = tables()
            self.assertIn("refs", tbls)
            self.assertTrue("refType" in tbls or "reftype" in tbls)

    def test_reset_db_clears_refs(self):
        with app.app_context():
            reset_db()
            create_reference("article", author="A", title="T", journal="J", year="2020")
            refs_before = get_references()
            self.assertGreaterEqual(len(refs_before), 1)
            reset_db()
            refs_after = get_references()
            self.assertEqual(len(refs_after), 0)

    def test_delete_reference_success_and_failure(self):
        with app.app_context():
            reset_db()
            create_reference("article", author="A", title="T", journal="J", year="2020")
            refs = get_references()
            rid = refs[0].id
            ok = delete_reference(rid)
            self.assertTrue(ok)
            ok2 = delete_reference(99999)
            self.assertFalse(ok2)

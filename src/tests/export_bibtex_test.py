import unittest
from config import app
from repositories.reference_repository import create_reference
from db_helper import reset_db
from app import export

class TestExportBibTeX(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        with app.app_context():
            reset_db()

            create_reference(
                "inproceedings",
                author="Export Author",
                title="Export Title",
                booktitle="Export Book",
                year="2024",
            )
            create_reference(
                "article",
                author="Second Author",
                title="Second Title",
                journal="Second Journal",
                year="2023",
            )

    def test_export_returns_bibtex_payload(self):

        with app.app_context():
            resp = export()

        if hasattr(resp, "get_data"):
            text = resp.get_data(as_text=True)
            status_code = getattr(resp, "status_code", 200)
            content_type = resp.headers.get("Content-Type", "")
        else:
            text = str(resp)
            status_code = 200
            content_type = "text/plain"

        self.assertEqual(status_code, 200)

        self.assertIn("@inproceedings{", text)
        self.assertIn("author = {Export Author}", text)
        self.assertIn("title = {Export Title}", text)
        self.assertIn("@article{", text)
        self.assertIn("author = {Second Author}", text)
        self.assertIn("title = {Second Title}", text)

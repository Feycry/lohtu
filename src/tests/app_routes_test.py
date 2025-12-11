import unittest
from config import app
from db_helper import reset_db, setup_db
from repositories.reference_repository import create_reference, get_references
import requests
from unittest.mock import patch, Mock


class TestAppRoutes(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with app.app_context():
            setup_db()
    def setUp(self):
        self.client = app.test_client()
        with app.app_context():
            reset_db()

    def test_index_page_renders(self):
        resp = self.client.get("/")
        self.assertEqual(resp.status_code, 200)
        text = resp.get_data(as_text=True)
        self.assertIn("Reference app", text)

    def test_index_with_query_shows_results_banner(self):
        with app.app_context():
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
        resp = self.client.get("/?q=graph")
        self.assertEqual(resp.status_code, 200)
        text = resp.get_data(as_text=True)
        self.assertIn("Results", text)
        self.assertIn("Graph Algorithms", text)
        self.assertNotIn("Data Structures", text)

    def test_new_reference_without_type(self):
        resp = self.client.get("/new_reference")
        self.assertEqual(resp.status_code, 200)
        text = resp.get_data(as_text=True)
        self.assertIn("Create a new reference", text)

    def test_new_reference_with_type_shows_type(self):
        resp = self.client.get("/new_reference?reference_type=inproceedings")
        self.assertEqual(resp.status_code, 200)
        text = resp.get_data(as_text=True)
        self.assertIn("@inproceedings", text)

    def test_create_reference_happy_path(self):
        payload = {
            "reference_type": "inproceedings",
            "author": "Test Author",
            "title": "Test Title",
            "booktitle": "Test Book",
            "year": "2024",
        }
        resp = self.client.post("/create_reference", data=payload, follow_redirects=True)
        self.assertEqual(resp.status_code, 200)
        text = resp.get_data(as_text=True)
        self.assertIn("Test Title", text)
        self.assertIn("Test Author", text)


    def test_edit_reference_get_and_update(self):

        with app.app_context():
            create_reference(
                "inproceedings",
                author="E",
                title="Editable",
                booktitle="Book",
                year="2024",
            )
            ref_id = get_references()[0].id


        resp = self.client.get(f"/edit_reference?reference_id={ref_id}")
        self.assertEqual(resp.status_code, 200)
        text = resp.get_data(as_text=True)
        self.assertIn("Edit reference", text)


        payload = {
            "reference_id": str(ref_id),
            "year": "2025",
            "author": "E",
            "title": "Editable",
            "booktitle": "Book",
        }
        resp2 = self.client.post("/update_reference", data=payload, follow_redirects=True)
        self.assertEqual(resp2.status_code, 200)
        text2 = resp2.get_data(as_text=True)
        self.assertIn("Year: 2025", text2)

    def test_delete_reference_missing_and_success(self):
        resp = self.client.post("/delete_ref", data={}, follow_redirects=True)
        self.assertEqual(resp.status_code, 200)
        with app.app_context():
            reset_db()
            create_reference(
                "inproceedings",
                author="Del",
                title="To Delete",
                booktitle="Book",
                year="2024",
            )
            ref_id = get_references()[0].id
        resp2 = self.client.post("/delete_ref", data={"reference_id": str(ref_id)}, follow_redirects=True)
        self.assertEqual(resp2.status_code, 200)
        text = resp2.get_data(as_text=True)
        self.assertNotIn("To Delete", text)
    def test_create_reference_success_redirects(self):
        payload = {
            "reference_type": "inproceedings",
            "author": "AA",
            "title": "Valid Title",
            "booktitle": "Conf",
            "year": "2024",
        }
        resp = self.client.post("/create_reference", data=payload)
        self.assertEqual(resp.status_code, 302)
        self.assertIn("/", resp.location)

    def test_update_reference_success(self):
        with app.app_context():
            reset_db()
            create_reference("inproceedings", author="E", title="Editable", booktitle="B", year="2024")
            from repositories.reference_repository import get_references
            ref_id = get_references()[0].id
        good = {
            "reference_id": str(ref_id),
            "author": "E",
            "title": "New Title",
            "booktitle": "B",
            "year": "2025",
        }
        resp_ok = self.client.post("/update_reference", data=good)
        self.assertEqual(resp_ok.status_code, 302)

    def test_export_selected_without_selection(self):
        with app.app_context():
            create_reference("article", author="A", title="T1", journal="J", year="2020")
            create_reference("article", author="B", title="T2", journal="J", year="2021")
        resp = self.client.get("/export_selected")
        self.assertIn(resp.status_code, (200, 302))

    def test_export_selected_with_selection(self):
        with app.app_context():
            reset_db()
            create_reference("article", author="A", title="T1", journal="J", year="2020")
            from repositories.reference_repository import get_references
            rid = get_references()[0].id
        resp = self.client.get(f"/export_selected?reference_id={rid}")
        self.assertEqual(resp.status_code, 200)
        self.assertIn("Content-Disposition", resp.headers)
        self.assertIn("@", resp.get_data(as_text=True))

    def test_export_all_bibtex(self):
        with app.app_context():
            reset_db()
            create_reference("article", author="A", title="T1", journal="J", year="2020")
        resp = self.client.get("/export")
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(resp.headers.get("Content-Type", "").startswith("text/plain"))
        self.assertIn("@article", resp.get_data(as_text=True))

    def test_lookup_doi_success_and_failure(self):
        fake_bib = "@article{1,\n  author = {John Doe},\n  title = {X},\n  journal = {J},\n  year = {2020}\n}"
        with patch("app.requests.get") as mget:
            resp_mock = Mock()
            resp_mock.text = fake_bib
            resp_mock.raise_for_status = Mock()
            mget.return_value = resp_mock
            resp = self.client.post("/lookup_doi", data={"doi": "10.1/x"})
            self.assertEqual(resp.status_code, 302)
            self.assertIn("/new_reference?", resp.location)
        resp2 = self.client.post("/lookup_doi", data={"doi": " "}, follow_redirects=True)
        self.assertEqual(resp2.status_code, 200)
        self.assertIn("DOI is required", resp2.get_data(as_text=True))

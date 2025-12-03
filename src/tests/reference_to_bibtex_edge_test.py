import unittest
from entities.reference import Reference


class TestReferenceToBibtexEdgeCases(unittest.TestCase):
    def test_empty_reference_returns_error_marker(self):
        ref = Reference(42)
        self.assertEqual(ref.to_bibtex(), "ERROR: Reference #42")

import unittest
from util import validate_reference, UserInputError

class TestsReferenceValiditation(unittest.TestCase):
    def setup(self):
        pass
    
    def test_valid_lenght(self):
        validate_reference("abc")
    
    def test_too_short(self):
        with self.assertRaises(UserInputError):
            validate_reference("")
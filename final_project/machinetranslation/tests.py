import unittest
from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):

    def test_translation_enfr(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
    
    def test_translation_fren(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

unittest.main()
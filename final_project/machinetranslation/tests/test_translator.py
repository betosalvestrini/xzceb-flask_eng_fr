import unittest
from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):

    def test_translation_enfr(self):
        self.assertNotEqual(english_to_french(''), None)
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
    
    def test_translation_fren(self):
        self.assertNotEqual(french_to_english(''), None)
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

unittest.main()
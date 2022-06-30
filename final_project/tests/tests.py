import unittest
from machinetranslation.translator import french_to_english, english_to_french

class EnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")
        self.assertEqual(english_to_french("By"), "Par")

class FrenchToEnlgish(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        self.assertEqual(french_to_english("Par"), "By")

unittest.main()
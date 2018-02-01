from trigrams import main
from trigrams import word_list
from trigrams import dict_build
from trigrams import word_builder
import unittest

class TestOne(unittest.TestCase):
    def test_one(self):
        self.assertEqual(word_list('test.txt'), ["this", "is", "a", "test"])
    
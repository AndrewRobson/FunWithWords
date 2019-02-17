from unittest import TestCase
from ..src.wordcounting import word_count
import os

TEST_FILE = 'testFile.txt'

class TestWordCount(TestCase):

    # # Check return type is a dictionary
    def test_word_count_is_instance(self):
        with open(TEST_FILE, 'w') as file:
            file.write('hello world how are you today')
        self.assertIsInstance(word_count(os.path.realpath(file.name),''), dict)

    # Some normal inputs producing regular results
    def test_word_count_normal(self):
        looking_for_words = ['hello', 'how', 'much', 'today']
        expected_dictionary = {'hello': 1, 'how': 1, 'much': 0, 'today': 1}
        with open(TEST_FILE, 'w') as file:
            file.write('hello world how are you today')

        self.assertDictEqual(word_count(os.path.realpath(file.name), looking_for_words), expected_dictionary)

    # Edge case: File is empty (counts stay zero)
    def test_empty_file(self):
        looking_for_words = ['how', 'now', 'brown', 'cow']
        expected_dictionary = {'how': 0, 'now': 0, 'brown': 0, 'cow': 0}
        with open(TEST_FILE, 'w') as file:
            pass # Do nothing so its an empty file

        self.assertDictEqual(word_count(os.path.realpath(file.name), looking_for_words), expected_dictionary)

    # Edge case: None of the search words occur (counts stay zero)
    def test_no_words_occur(self):
        looking_for_words = ['how', 'now', 'brown', 'cow']
        expected_dictionary = {'how': 0, 'now': 0, 'brown': 0, 'cow': 0}
        with open(TEST_FILE, 'w') as file:
            file.write('hello world its too hot today')

        self.assertDictEqual(word_count(os.path.realpath(file.name), looking_for_words), expected_dictionary)

    # Edge case: File can't be found (should raise exception)
    def test_no_file_found(self):
        looking_for_words = ['this', 'is', 'a', 'test']
        with self.assertRaises(FileNotFoundError):
            word_count('filesDoesNotExist.txt', looking_for_words)

    # Cleanup method for tests
    def tearDown(self):
        # Check if file exists if so then clean it up
        if os.path.isfile(TEST_FILE): os.remove(TEST_FILE)
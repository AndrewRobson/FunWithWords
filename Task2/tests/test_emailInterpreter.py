from unittest import TestCase
from Task2.src.EmailInterpreter import EmailInterpreter
import os

TEST_FILE = 'testFile.txt'

DIRECTORY_PATH = 'inputFiles'
OUTPUT_DIRECTORY_PATH = 'outputFiles'

class TestEmailInterpreter(TestCase):

    def setUp(self):
        self.example_class = EmailInterpreter()
        self.example_class.threshold = 0.6
        self.example_class.directory_path = DIRECTORY_PATH

        if not os.path.exists(DIRECTORY_PATH):
            os.makedirs(DIRECTORY_PATH)
        if not os.path.exists(OUTPUT_DIRECTORY_PATH):
            os.makedirs(OUTPUT_DIRECTORY_PATH)

    def test_find_common(self):
        with open(os.path.join(DIRECTORY_PATH, TEST_FILE), 'w') as file:
            file.write('Hello John, how are you today?\n')
            file.write('Its pretty hot today. Bring on the winter time!\n')
            file.write('Yes I love the snow we get during winter.\n')

        example_class = EmailInterpreter()
        with self.assertRaises(NotImplementedError):
            example_class.split_file(file)

    def test_strip_common(self):
        with open(os.path.join(DIRECTORY_PATH, TEST_FILE), 'w') as file:
            file.write('Hello John, how are you today?\n')
            file.write('Its pretty hot today. Bring on the winter time!\n')
            file.write('Yes I love the snow we get during winter.\n')

        example_class = EmailInterpreter()
        with self.assertRaises(NotImplementedError):
            example_class.split_file(file)

    # Check that when no files are present the logic doesn't break and it returns 0
    def test_filter_lines_empty(self):
        self.example_class.filter_lines(['Line 1', 'Line 2'])
        self.assertEqual(len(self.example_class.common_lines), 0)

    def test_filter_lines_normal(self):
        self.example_class.file_count = 5
        output = self.example_class.filter_lines(['Line 1', 'Line 2', 'Line 1', 'Line 1', 'Line 2', 'Line 1'])
        self.assertEqual(len(output), 1)

    # Check that the default split file function returns Not Implemented Error
    def test_split_file(self):
        with open(os.path.join(DIRECTORY_PATH, TEST_FILE), 'w') as file:
            file.write('Hello John, how are you today?\n')
            file.write('Its pretty hot today. Bring on the winter time!\n')
            file.write('Yes I love the snow we get during winter.\n')

        example_class = EmailInterpreter()
        with self.assertRaises(NotImplementedError):
            example_class.split_file(file)

    def tearDown(self):
        # Check if file exists if so then clean it up
        if os.path.isfile(os.path.join(DIRECTORY_PATH, TEST_FILE)): os.remove(os.path.join(DIRECTORY_PATH, TEST_FILE))



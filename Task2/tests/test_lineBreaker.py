from unittest import TestCase
from Task2.src.LineBreaker import LineBreaker
import os
import filecmp

TEST_FILE = 'testFile.txt'
TEST_FILE_ONE = 'testFileOne.txt'
TEST_FILE_TWO = 'testFileTwo.txt'
TEST_FILE_THREE = 'testFileThree.txt'

STRIPPED_OUTPUT_FILE = 'copy_' + TEST_FILE_ONE

SIGNATURE_LINE = 'Kind Regards,\nAndrew Robson.\n0211860336.\n'
SIGNATURE_LINE_TWO = 'Regards,\nJohn Taker.\n0211837488.\n'
GREETING_LINE = 'Dear John,\n'
GREETING_LINE_TWO = 'Dear Andrew,\n\n'
QUESTION_LINE = 'I wanted to know how you are getting on with the programming task\n'
FINISHING_LINE = 'Please let me know if you have any questions or concerns\n\n'
TEST_LINE = 'This is a test\n'

DIRECTORY_PATH = 'inputFiles'
OUTPUT_DIRECTORY_PATH = 'outputFiles'


class TestLineBreaker(TestCase):
    def setUp(self):
        self.example_class = LineBreaker()
        self.example_class.threshold = 0.6
        self.example_class.directory_path = DIRECTORY_PATH
        self.example_class.destination_directory_path = OUTPUT_DIRECTORY_PATH

        if not os.path.exists(DIRECTORY_PATH):
            os.makedirs(DIRECTORY_PATH)
        if not os.path.exists(OUTPUT_DIRECTORY_PATH):
            os.makedirs(OUTPUT_DIRECTORY_PATH)

    # Separated out this creation of test files so that I can easily choose when I want to make files
    # and so that I can test for cases where I don't want any files
    def create_test_files(self):
        # Creating a test file
        with open(os.path.join(DIRECTORY_PATH, TEST_FILE_ONE), 'w') as file:
            file.writelines([GREETING_LINE, QUESTION_LINE, FINISHING_LINE, TEST_LINE, SIGNATURE_LINE])
        # Creating a test file
        with open(os.path.join(DIRECTORY_PATH, TEST_FILE_TWO), 'w') as file:
            file.writelines([GREETING_LINE_TWO, 'Yes its going well, im having fun doing it!\n', TEST_LINE,
                             'Ill get it completed to you as soon as possible.\n', SIGNATURE_LINE_TWO])
        # Creating a test file
        with open(os.path.join(DIRECTORY_PATH, TEST_FILE_THREE), 'w') as file:
            file.writelines([GREETING_LINE_TWO, 'Please find attached my completed programming task.\n',
                             'I look forward to hearing back from you about your thoughts.\n', SIGNATURE_LINE_TWO])
        # Creating a expected example outfile
        with open(os.path.join(OUTPUT_DIRECTORY_PATH, STRIPPED_OUTPUT_FILE), 'w') as file:
            file.writelines([GREETING_LINE, QUESTION_LINE, FINISHING_LINE, SIGNATURE_LINE])

    def test_find_common(self):
        self.create_test_files()

        self.example_class.find_common()
        self.assertEqual(len(self.example_class.common_lines), 6)

    def test_find_common_empty_directory(self):
        self.example_class.find_common()
        self.assertEqual(len(self.example_class.common_lines), 0)

    def test_strip_common(self):
        self.create_test_files()

        self.example_class.common_lines = [GREETING_LINE, TEST_LINE]
        self.example_class.strip_common(TEST_FILE_ONE)
        self.assertTrue(filecmp.cmp(os.path.join(OUTPUT_DIRECTORY_PATH, STRIPPED_OUTPUT_FILE), os.path.join(OUTPUT_DIRECTORY_PATH, 'copy_' + TEST_FILE_ONE)))

    def test_split_file(self):
        with open(TEST_FILE, 'w') as file:
            file.write('Hello John, how are you today?\n')
            file.write('Its pretty hot today. Bring on the winter time!\n')
            file.write('Yes I love the snow we get during winter.\n')

        expected_result = ['Hello John, how are you today?\n', 'Its pretty hot today. Bring on the winter time!\n',
                           'Yes I love the snow we get during winter.\n']
        example_class = LineBreaker()
        self.assertListEqual(example_class.split_file(os.path.realpath(file.name)), expected_result)

    # Cleanup method for tests
    def tearDown(self):
        if os.path.exists(DIRECTORY_PATH):
            for file in os.listdir(DIRECTORY_PATH):
                os.remove(os.path.join(DIRECTORY_PATH, file))
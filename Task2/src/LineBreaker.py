from Task2.src.EmailInterpreter import EmailInterpreter
import os
# Part B:
# -------
# Write a child-class of the previously written base class, which
# implements the 'split_file' function, simply by treating each line as a
# unit (it returns the list of lines).
class LineBreaker(EmailInterpreter):
    def split_file(self, file_name):
        with open(os.path.join(self.directory_path, file_name), 'r') as file:
            lines = file.readlines()
            return lines
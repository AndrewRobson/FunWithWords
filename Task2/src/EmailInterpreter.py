import os

# Remove common lines from a set of files
# an example email signatures
class EmailInterpreter:
    def __init__(self):
        # 2. When the class is instantiated, the following parameters should
        # be provided:
        # * An 'input directory path' (the name of an existing directory).
        # * A 'threshold' (the threshold is a float number between 0 and 1).
        # * A 'destination directory path' (the name of an existing directory
        #   into which filtered output should be written).
        self.directory_path = ''
        self.threshold = 0 # this is a percentage based thing
        self.destination_directory_path = ''
        self.common_lines = []
        self.file_count = 0

    def find_common(self):
        # 3. * Should read all the files in the source directory.
    # * For each file, it should use the 'split_file' function to return
    #   the smaller 'units' that make up the file (for example lines).
    # * It should find all units, which occur in a higher percentage
    #   of input files than indicated via the threshold parameter. For
    #   example, if the threshold value is 0.6 then any unit occurring in
    #   more than 60% of the source files would be detected. Any unit which
    #   occurs that often is deemed 'common'.
    # * The function should store a list of all common units in the class
    #   instance.

        # 1 get all the files
        # assuming its only the files in directory and not sub folders if there are any
        # read them?
        files = os.listdir(self.directory_path)
        self.file_count = len(files)
        combined_files = []
        # 2 split file for each file calling
        for file in files:
            combined_files += self.split_file(file)

        # store list of all common units in the class instance
        self.common_lines = self.filter_lines(combined_files)

    def strip_common(self, file):
        # This function should write a copy of each of the input files
        # into the destination file (using the same file name), but those
        # copies should not contain any units, which were deemed to be
        # common (as stored in the class).
        file_lines = self.split_file(file)
        file_name = 'copy_' + file

        with open(os.path.join(self.directory_path, file_name), 'w') as file:#todo write to directory
            for file_line in file_lines:
                if not file_line in self.common_lines:
                    file.write(file_line)

    def filter_lines(self, file_lines):
        # loop through lines removing common
        line_dictionary = {key: 0 for key in file_lines}
        for line in file_lines:
            line_dictionary[line] += 1  # todo check if we need to initialise this or maybe can just do this, think we do need to init it

        # find all units based on threshold param
        common_lines = []
        for key in line_dictionary:
            if line_dictionary[key] >= (self.threshold * self.file_count):
                common_lines.append(key)

        return common_lines

    def split_file(self, file_name):
        raise NotImplementedError


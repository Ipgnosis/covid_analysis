# the Ipgnosis Logger class

import json
import os


class Ipgn_Logger:

    # initialize the class instance
    def __init__(self, log_file_path):
        self.log_file_path = log_file_path

        self.configure_logging()

    # configure the logging schema
    def configure_logging(self):

        self.logging_config = self.read_file('logging_config.json')
        pass

    # read data file
    def read_file(self, fname):

        path = os.path.join(self.log_file_path, fname)

        try:
            with open(path, 'r') as f:
                return json.load(f)
        except OSError as error:
            print(error)
            # this should be a logged event
            print("File {} read failed.", format(fname))

            return False

    # write file from data in data_struct

    def write_file(self, fname, this_data):

        path = os.path.join(self.log_file_path, fname)

        try:
            with open(path, 'w') as f:
                json.dump(this_data, f)
            f.close()

            return True

        except OSError as error:
            print(error)
            # this should be a logged event
            print("File {} cannot be saved.".format(fname))

            return False

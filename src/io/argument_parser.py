import argparse

class ArgumentParser:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description='Album Maker')
        self._add_args()
        self.parser.parse_args()

    def _add_args(self):
        self.parser.add_argument('URL', help='Enter the album URL from youtube')
        self.parser.add_argument('CSV', help='Enter the path of timestamps CSV file')
        self.parser.add_argument('-v', '--verbose', help='provides verbose output for youtube_dl', action='store_true')

    def get_url(self):
        return self.parser.parse_args().URL

    def is_verbose(self):
        return self.parser.parse_args().verbose

    def get_csv(self):
        return self.parser.parse_args().CSV
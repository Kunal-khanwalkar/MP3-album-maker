import argparse

class ArgumentParser:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description='Album Maker')
        self.addArgs()
        self.parser.parse_args()

    def addArgs(self):
        self.parser.add_argument('URL', help='Enter the album URL from youtube')
        self.parser.add_argument('--verbose', help='provides verbose output for youtube_dl', action='store_true')

    def getURL(self):
        return self.parser.parse_args().URL

    def getOpts(self):
        return self.parser.parse_args().verbose
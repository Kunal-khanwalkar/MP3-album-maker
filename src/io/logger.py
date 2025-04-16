class Logger(object):
    def __init__(self, is_verbose):
        self.is_verbose = is_verbose

    def debug(self, msg):
        if self.is_verbose:
            print(f"[DEBUG]: {msg}")

    def warn(self, msg):
        print(f"[WARN]: {msg}")

    def error(self, msg):
        print(f"[ERROR]: {msg}")
class Logger(object):
    def __init__(self, is_verbose):
        self.is_verbose = is_verbose

    def debug(self, msg, *args):
        if self.is_verbose:
            print(f"\033[92m[DEBUG]\033[0m: {msg} {' '.join(map(str, args))}")

    def warn(self, msg, *args):
        print(f"\033[93m[WARN]\033[0m: {msg} {' '.join(map(str, args))}")

    def error(self, msg, *args):
        print(f"\033[91m[ERROR]\033[0m: {msg} {' '.join(map(str, args))}")
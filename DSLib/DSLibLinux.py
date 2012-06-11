import sys

# When I install Linux I will make it.
class DSLibLinux():
    def __init__(self, key):
        if not sys.platform.startswith("linux"):
            raise Exception, "I really think that you want to use another library compatible with your system ;)"
        raise Exception("Not developed.")
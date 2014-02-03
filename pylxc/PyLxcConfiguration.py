import os
import os.path

class PyLxcConfiguration(object):
    def __init__(self):
        pass

    def getDefaultCacheConfiguration(self):
        return os.path.join(os.path.expanduser('~'), '.cache', 'pylxc')

config = PyLxcConfiguration()
def get():
    return config

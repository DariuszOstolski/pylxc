import os
import platform

def iscallable(obj):
    return hasattr(obj, '__call__') or hasattr(obj, '__bases__')

class PyLxcConfigurationOption(object):
    """
    """
    def __init__(self,  **kwargs):
        self.section = kwargs.pop('section', 'global')
        self.help = kwargs.pop('help', '')
        self.dest = kwargs.pop('dest')
        self.default = kwargs.pop('default', lambda: None)
        if not iscallable(self.default):
            raise TypeError("default is not callable")
        self.options = None
        self.environment = None
        if kwargs.has_key('options'):
            self.options = kwargs.pop('options')

        if kwargs.has_key('env_var'):
            self.environment = kwargs.pop('env_var')


class PyLxcConfiguration(object):

    Architecture = PyLxcConfigurationOption(section='global',
                                            help="LXC guest architecture",
                                            options='--architecture',
                                            default=getDefaultArch)

    Cache = PyLxcConfigurationOption(section='global',
                           options=['-c', '--cache-directory'],
                           help='Path to cache directory',
                           default=getDefaultCacheConfiguration,
                           dest='Cache')


    def __init__(self):
        pass

    def getDefaultCacheConfiguration(self):
        return os.path.join(os.path.expanduser('~'), '.cache', 'pylxc')

    def getDefaultArch(self):
        return platform.processor()



config = PyLxcConfiguration()
def get():
    return config

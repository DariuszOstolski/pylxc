import os
import platform

def iscallable(obj):
    return hasattr(obj, '__call__') or hasattr(obj, '__bases__') or callable(obj)

class PyLxcConfigurationOption(object):
    """
    """
    def __init__(self,  **kwargs):
        self.section = kwargs.pop('section', 'global')
        self.help = kwargs.pop('help', '')
        self.dest = kwargs.pop('dest', None)
        self.default = kwargs.pop('default', lambda: None)
        if not iscallable(self.default):
            raise TypeError("default is not callable")
        self.options = kwargs.pop('options', None)
        self.environment = kwargs.pop('env_var', None)
        self.value = kwargs.pop('value', None)

    def getVariableName(self, owner):
         for attr in dir(owner):
            if getattr(owner, attr) is self:
                return attr

    def __get__(self, obj, objtype):

        if obj is None:
            return self
        if self.dest is None:
            self.dest = self.getVariableName(objtype)

        if self.value is not None:
            return self.value
        if self.default is not None:
            return self.default()
        return None

    def __set__(self, obj, objtype):
        if self.dest is None:
            self.dest = self.getVariableName(objtype)
        self.value = obj



def getDefaultCacheConfiguration():
    return os.path.join(os.path.expanduser('~'), '.cache', 'pylxc')


def getDefaultArch():
    return platform.processor()


class PyLxcConfiguration(object):

    def __init__(self):
        pass


    Architecture = PyLxcConfigurationOption(section='global',
                                            help="LXC guest architecture",
                                            options='--architecture',
                                            default=getDefaultArch)

    Cache = PyLxcConfigurationOption(section='global',
                           options=['-c', '--cache-directory'],
                           help='Path to cache directory',
                           default=getDefaultCacheConfiguration)




config = PyLxcConfiguration()
def get():
    return config

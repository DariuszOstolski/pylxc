import LXCPlugin
import logging
import PyLxcConfiguration


log = logging.getLogger("pylxc.gentoo")

class LXCDefaultConfig(PyLxcConfiguration.PyLxcConfiguration):
    """

    """

    PythonToGentooArchs = dict(x86_64='amd64', i386='x86')
    def __init__(self):
        PyLxcConfiguration.PyLxcConfiguration.__init__(self, *args, **kwargs)

    def getStageUrl(self):
        pass




class LXCGentooCommand(LXCPlugin.LXCPluginCommand):
    """

    """
    def __init__(self):
        pass
    def __call__(self, parsedArgs, lxcConfiguration):
        log.info("LXC gentoo guest plugin")
        log.debug("Args: {0}".format(parsedArgs))

def create(*args, **kwargs):
    log.info("Creating lxc gentoo guest")

class LXCGentooPlugin(LXCPlugin.LXCPlugin):
    def __init__(self, *args, **kwargs):
        LXCPlugin.LXCPlugin.__init__(self, *args, **kwargs)

    def register(self, argParser):
        LXCPlugin.LXCPlugin.register(self, argParser)
        subParser = argParser.addSubParser('gentoo', help="LXC gentoo managment")
        subParser.add_argument('create', help='Create lxc gentoo guest container')

        subParser.setMainModule(LXCGentooCommand())


def createPlugin(*args, **kwargs):
    return LXCGentooPlugin(*args, **kwargs)

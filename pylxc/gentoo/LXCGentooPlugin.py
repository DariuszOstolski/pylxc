from  LXCPlugin import LXCPlugin
import logging

log = logging.getLogger("pylxc.gentoo")

def create(*args, **kwargs):
    log.info("Creating lxc gentoo guest")

class LXCGentooPlugin(LXCPlugin):
    def __init__(self, *args, **kwargs):
        LXCPlugin.__init__(self, *args, **kwargs)

    def register(self, argParser):
        LXCPlugin.register(self, argParser)
        subParser = argParser.addSubParser('gentoo', help="LXC gentoo managment")
        subParser.add_argument('create', help='Create lxc gentoo guest container')
        subParser.setMainModule(create)


def createPlugin(*args, **kwargs):
    return LXCGentooPlugin(*args, **kwargs)

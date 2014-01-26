import sys
import argparse
from logger import logger
import logging

class LXCPluginsScanner(object):
    SUPPORTED_LXC_CONTAINERS = ['gentoo']
    def __init__(self):
        pass

    def importPlugins(self):
        pass

class SubParser(argparse.ArgumentParser):
    def __init__(self, **kwargs):
        super(argparse.ArgumentParser, self).__init__(kwargs)

    def setMainModule(self, mainModule):
        self._subParserModule.set_defaults(commandMainModule=mainModule)


class ArgumentParser(argparse.ArgumentParser):
    def __init__(self, *args, **kwargs):
        argparse.ArgumentParser.__init__(self,*args, **kwargs)
        self._subParsers = self.add_subparsers(dest="moduleName",
                                               help="Distribution name to be prepared for lxc deployment")

    def addSubparser(self, *args, **kwargs):
        subParser = self.add_parser(*args, **kwargs)
        return SubParser(subParser)


def main(argv = None):
    if argv is None:
        argv = sys.argv

    argParser = ArgumentParser()
    argParser.add_argument( '--verbose', '-v', action='count', help="Log more detailed output")
    options = argParser.parse_args(argv)
    if options.verbose<1:
        logger.getLogger().setLevel(logging.ERROR)
    elif options.verbose<2:
        logger.getLogger().setLevel(logging.DEBUG)
    else:
        logger.getLogger().setLevel(logging.INFO)



if __name__ == "__main__":
    sys.exit(main())
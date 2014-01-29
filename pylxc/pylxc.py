import sys
import argparse
from logger import logger
import logging
import types
import importlib


log = logging.getLogger("pylxc.main")

class LXCPluginsLoader(object):
    SUPPORTED_LXC_CONTAINERS = ['gentoo']
    def __init__(self):
        pass

    def importPlugins(self, argParser):
        for moduleName in LXCPluginsLoader.SUPPORTED_LXC_CONTAINERS:
            try:
                module = importlib.import_module(moduleName)
                plugin = module.createPlugin()
                plugin.register(argParser)
            except ImportError as error:
                log.error("Cannot import {0}: {1} ".format(moduleName, error))


class ArgumentParser(argparse.ArgumentParser):
    def __init__(self, *args, **kwargs):
        argparse.ArgumentParser.__init__(self, *args, **kwargs)
        self._subParsers = self.add_subparsers(dest="moduleName",
                                               title="Supported lxc guests",
                                               description="Supported lxc guests",
                                               help="Distribution name to be prepared for lxc deployment",
                                               parser_class=argparse.ArgumentParser)

    def addSubParser(self, *args, **kwargs):
        subParser = self._subParsers.add_parser(*args, **kwargs)
        #extend subParser with setMainModule
        def setMainModule(self, mainModuleName):
            self.set_defaults(executeCommand=mainModuleName)
        subParser.setMainModule = types.MethodType(setMainModule, subParser)
        return subParser


def main(argv = None):
    if argv is None:
        argv = sys.argv[1:]

    argParser = ArgumentParser()
    argParser.add_argument( '--verbose', '-v', action='count', help="Log more detailed output")
    loader = LXCPluginsLoader()
    loader.importPlugins(argParser)

    options = argParser.parse_args(argv)
    if options.verbose<1:
        logger.getLogger().setLevel(logging.ERROR)
    elif options.verbose<2:
        logger.getLogger().setLevel(logging.DEBUG)
    else:
        logger.getLogger().setLevel(logging.INFO)

    options.executeCommand(options, None)


if __name__ == "__main__":
    sys.exit(main())
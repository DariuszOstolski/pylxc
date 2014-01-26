import logging
import os

logFormat = "[%(levelname)s] %(name)s %(message)s"

def initializeLogger(outputDir):
    logger = getLogger()
    logger.setLevel(logging.DEBUG)

    # create error file handler and set level to error
    handler = logging.FileHandler(os.path.join(outputDir, "error.log"),"w", encoding=None, delay="true")

    handler.setLevel(logging.ERROR)
    formatter = logging.Formatter(logFormat)
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    # create debug file handler and set level to debug
    handler = logging.FileHandler(os.path.join(outputDir, "all.log"),"w")
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter(logFormat)
    handler.setFormatter(formatter)
    logger.addHandler(handler)


logger = logging.getLogger('pylxc')
logger.setLevel(logging.INFO)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter(logFormat)

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)


def getLogger():
    return logger

import LXCGentooPlugin

def createPlugin(*args, **kwargs):
    gentoo = LXCGentooPlugin.createPlugin(*args, **kwargs)
    return gentoo
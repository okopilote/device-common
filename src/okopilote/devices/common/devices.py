import configparser
from importlib import import_module


_conf_file = None
_devices = {}


class DeviceError(Exception):
    """Generic devices package error"""


def config_file(filepath):
    global _conf_file
    global _devices
    _conf_file = filepath
    _devices.clear()


def get_device(name):
    global _conf_file
    global _devices

    if not _conf_file:
        raise DeviceError("No config file specified")
    if not name:
        return None
    elif name not in _devices:
        conf = configparser.ConfigParser()
        conf.read_file(open(_conf_file))
        module = import_module(conf[name]["module"])
        _devices[name] = module.from_conf(conf[name])

    return _devices[name]

import ctypes

from core.pytensions.slots_proxy import SlotsProxy


def patch(type):
    name = type.__name__
    target = type.__dict__

    proxy_dict = SlotsProxy.from_address(id(target))
    namespace = {}

    ctypes.pythonapi.PyDict_SetItem(
        ctypes.py_object(namespace),
        ctypes.py_object(name),
        proxy_dict.dict)
    return namespace[name]

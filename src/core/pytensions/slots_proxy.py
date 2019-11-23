import ctypes

from core.pytensions.pyobject import PyObject


class SlotsProxy(PyObject):
    _fields_ = [('dict', ctypes.POINTER(PyObject))]

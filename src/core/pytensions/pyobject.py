import ctypes


class PyObject(ctypes.Structure):
    pass


PyObject._fields_ = [
    ('ob_refcnt', ctypes.c_int),
    ('ob_type', ctypes.POINTER(PyObject)),
]

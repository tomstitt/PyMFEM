# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.1
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _hash
else:
    import _hash

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


import mfem._par.array
import mfem._par.mem_manager
import mfem._par.vector
class Hashed2(object):
    r"""Proxy of C++ mfem::Hashed2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    p1 = property(_hash.Hashed2_p1_get, _hash.Hashed2_p1_set, doc=r"""p1 : int""")
    p2 = property(_hash.Hashed2_p2_get, _hash.Hashed2_p2_set, doc=r"""p2 : int""")
    next = property(_hash.Hashed2_next_get, _hash.Hashed2_next_set, doc=r"""next : int""")

    def __init__(self):
        r"""__init__(Hashed2 self) -> Hashed2"""
        _hash.Hashed2_swiginit(self, _hash.new_Hashed2())
    __swig_destroy__ = _hash.delete_Hashed2

# Register Hashed2 in _hash:
_hash.Hashed2_swigregister(Hashed2)

class Hashed4(object):
    r"""Proxy of C++ mfem::Hashed4 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    p1 = property(_hash.Hashed4_p1_get, _hash.Hashed4_p1_set, doc=r"""p1 : int""")
    p2 = property(_hash.Hashed4_p2_get, _hash.Hashed4_p2_set, doc=r"""p2 : int""")
    p3 = property(_hash.Hashed4_p3_get, _hash.Hashed4_p3_set, doc=r"""p3 : int""")
    next = property(_hash.Hashed4_next_get, _hash.Hashed4_next_set, doc=r"""next : int""")

    def __init__(self):
        r"""__init__(Hashed4 self) -> Hashed4"""
        _hash.Hashed4_swiginit(self, _hash.new_Hashed4())
    __swig_destroy__ = _hash.delete_Hashed4

# Register Hashed4 in _hash:
_hash.Hashed4_swigregister(Hashed4)


def sort3(a, b, c):
    r"""sort3(int & a, int & b, int & c)"""
    return _hash.sort3(a, b, c)

def sort4(a, b, c, d):
    r"""sort4(int & a, int & b, int & c, int & d)"""
    return _hash.sort4(a, b, c, d)


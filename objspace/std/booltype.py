from pypy.interpreter import gateway
from pypy.objspace.std.stdtypedef import StdTypeDef
from pypy.objspace.std.inttype import int_typedef

def descr__new__(space, w_booltype, w_obj=None, w_symbolic=False):
    space.w_bool.check_user_subclass(w_booltype)
    if space.is_true(w_obj):
        res = space.w_True        
    else:
        res = space.w_False
    res.set_symbolic(w_symbolic)
    return res

# ____________________________________________________________

bool_typedef = StdTypeDef("bool", int_typedef,
    __doc__ = '''bool(x) -> bool

Returns True when the argument x is true, False otherwise.
The builtins True and False are the only two instances of the class bool.
The class bool is a subclass of the class int, and cannot be subclassed.''',
    __new__ = gateway.interp2app(descr__new__),
    )
bool_typedef.acceptable_as_base_class = False

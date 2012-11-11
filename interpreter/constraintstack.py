"""
Implementation of the constraint stack.
"""

class Constraint(object):
    """
    This class is an abstract representation of
    a constraint.
    """
    __rvalue = None
    __lvalue = None
    __op = None
    __connective = None

    def __init__(self, l, r, op):
        self.__rvalue = r
        self.__lvalue = l
        self.__op = op

    def set_connective(self, conn):
        self.__connective = conn

    def __str__(self):
        return "%s %s %s" self.__lvalue, self.__op, self.__rvalue

class ConstraintStack(object):
    def __init__(self):
        self.items = []

    def pop(self):
        return self.items.pop()

    def push(self, constraint):
        self.items.append(constraint)

    def peek(self):
        return self.items[len(self.items)]

    def get_constr(self):
        retval = ""
        for constr in self.items:
            retval += constr.__lvalue + \
                constr.__op + constr.__rvalue
            if constr.__connective is not None:
                retval += constr.__connective
        return retval

    def set_conn_on_tos(self, conn):
        top = self.pop()
        top.__connective = conn
        self.push(top)


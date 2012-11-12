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
    __negated = False

    def __init__(self, l, r, op):
        self.__rvalue = r
        self.__lvalue = l
        self.__op = op

    def set_connective(self, conn):
        self.__connective = conn

    def __str__(self):
        s = self.__lvalue + " " + self.__op + " " + self.__rvalue
        if self.__negated:
            s = "not " + s
        return s

    def lvalue(self):
        return self.__lvalue

    def rvalue(self):
        return self.__rvalue

    def op(self):
        return self.__op

    def conn(self):
        return self.__connective

    def negate(self):
        self.__negated = not self.__negated

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
            retval += str(constr) + " "
            if constr.conn() is not None:
                retval += constr.conn()
        return retval

    def set_conn_on_tos(self, conn):
        top = self.pop()
        top.__connective = conn
        self.push(top)


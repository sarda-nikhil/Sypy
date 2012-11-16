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
    __explored = False

    def __init__(self, l, r, op):
        self.__rvalue = r
        self.__lvalue = l
        self.__op = op

    def set_connective(self, conn):
        self.__connective = conn

    def __str__(self):
        s = self.__lvalue + " " + self.__op + " " + self.__rvalue
        return s

    def lvalue(self):
        return self.__lvalue

    def rvalue(self):
        return self.__rvalue

    def augment_lvalue(self, s):
        return Constraint("not " + self.lvalue(), \
                              self.rvalue(), self.op())

    def op(self):
        return self.__op

    def conn(self):
        return self.__connective

    def explored(self):
        self.__explored = not self.__explored

    def is_explored(self):
        return self.__explored

class ConstraintStack(object):
    """
    The constraint stack helps keep track of all the constraints that
    need to be satisfied in order to jump to a target location.

    The constraint stack looks like [([constr1, constr2], insn), ...]
    """
    def __init__(self):
        self.items = []

    def pop(self, insn):
        if len(self.items) == 0:
            return None
        for constr_list, instr in self.items:
            if instr == insn:
                constr_list = []
                return

    def push(self, constraint, insn):
        for constr_list, instr in self.items:
            if instr == insn:
                constr_list.append(constraint)
                return
        self.items.append(([constraint], insn))

    def peek(self):
        if len(self.items) < 1:
            return (None, 0)
        return self.items[len(self.items) - 1]

    def get_constr(self, insn):
        retval = ""
        for constr_list, instr in self.items:
            if instr > insn:
                break;
            if len(constr_list) == 0:
                continue
            for c in constr_list:
                retval += c.lvalue() + " " + c.op() + " " + c.rvalue()
        return retval

    def set_conn_on_tos(self, conn):
        top = self.pop()
        top.__connective = conn
        self.push(top)

    def clear(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def get_constraints(self, insn):
        for constr_list, instr in self.items:
            if instr == insn:
                if len(constr_list) == 0:
                    break
                for c in constr_list:
                    if c.is_explored():
                        continue
                    c.explored()
                    yield c
    
    def get_constr(self, insn):
        # Get the constraint list associated with an insn
        for constr_list, instr in self.items:
            if instr == insn:
                return constr_list

    def is_assoc_insn(self, c, insn):
        constr_list = get_constr(self, insn)
        if constr_list is None:
            return False
        if c in get_constr(self, insn):
            return True
        return False

    def print_stack(self):
        for constr, insn in self.items:
            print "Constraints at fork " + str(insn)
            for c in constr:
                print str(c)

    def remove_stale_constraints(self, exec_stack, insn):
        print "Insn to remove: " + str(insn)
        constr_list = self.get_constr(insn)
        if constr_list is None:
            return exec_stack
        for c in exec_stack:
            if c in constr_list:
                idx = exec_stack.index(c)
                return exec_stack[:idx]
        return exec_stack

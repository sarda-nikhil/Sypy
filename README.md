Sypy: A symbolic execution engine for Python.

Sypy leverages PyPy's interpreter to interpret Python bytecode and generate constraints. These constraints are solved using
Microsoft's Z3 SMT solver.

Currently Sypy generates constraints for if statements involving integer values. While booleans, longs and floats have symbolic support they
have not been tested yet. Function evaluation has not been tested yet. Besides, supporting arbitrary functions is probably not a good idea.

The most appropriate way would be to determine all possible return values of a function and substitute those values in the constraints.


TODO:

The most important thing to do right now is to interleave symbolic execution code in the binary operations.
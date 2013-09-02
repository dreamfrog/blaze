"""
Blaze expression graph for deferred evaluation. Each expression node has
an opcode and operands. An operand is a Constant or another expression node.
Each expression node carries a DataShape as type.
"""

from functools import partial

#------------------------------------------------------------------------
# Opcodes
#------------------------------------------------------------------------

array = 'array'   # array input
kernel = 'kernel' # kernel application, carrying the blaze kernel as a
                  # first argument (Constant)

#------------------------------------------------------------------------
# Graph
#------------------------------------------------------------------------

class Op(object):
    """
    Single node in blaze expression graph.
    """

    def __init__(self, opcode, dshape, *args, **metadata):
        self.opcode = opcode
        self.dshape = dshape
        self.args   = list(args)
        self.metadata = metadata

    def __repr__(self):
        subtrees = " -+- ".join(map(str, self.args))
        node = "%s(%s){%s}" % (self.opcode, self.dshape, ", ".join(self.metadata))
        length = max(len(subtrees), len(node))
        return "%s\n%s" % (node.center(len(subtrees) / 2), subtrees.center(length))

# ______________________________________________________________________
# Graph constructors

ArrayOp    = partial(Op, array)
KernelOp   = partial(Op, kernel)
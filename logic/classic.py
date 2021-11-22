# Sets of possible symbols for connectives:
NOT = frozenset({'~', '¬', '-'})
AND = frozenset({'&', '^', '.'})
OR = frozenset({'+', 'v'})
IF_THEN = frozenset({'>', '->'})
IFF = frozenset({'=', '<->'})

UNARY = NOT
BINARY = AND | OR | IF_THEN | IFF

# Evaluate function:

def evaluate(tree, assign):
    if tree.left == None : return assign[tree.node]
    elif tree.right == None :
        if tree.node in NOT :
            return not evaluate(tree.left, assign)
        else :
            print('Error: non-classic connective')
            return -1
    else :
        if tree.node in AND :
            return evaluate(tree.left, assign) and evaluate(tree.right, assign)
        elif tree.node in OR :
            return evaluate(tree.left, assign) or evaluate(tree.right, assign)
        elif tree.node in IF_THEN :
            return (not evaluate(tree.left, assign)) or evaluate(tree.right, assign)
        elif tree.node in IFF :
            return not (evaluate(tree.left, assign) ^ evaluate(tree.right, assign))
        else :
            print('Error: non-classic connective')
            return -1

def nextAssignment(assign):
    for p in assign :
        if not assign[p] :
            assign[p] = True
            return assign
        else:
            assign[p] = False
    print('Error: there is no next assignment')
    return -1

def isValid(tree):
    "Verifies if a formula is valid. Reads a FormulaTree object and returns a Boolean."
    atoms = tree.atoms()
    assign = {a : False for a in atoms}
    if not evaluate(tree, assign) : return False
    while False in assign.values() :
        assign = nextAssignment(assign)
        if not evaluate(tree, assign):
            return False
    return True

def isSatisfiable(tree):
    "Verifies if a formula is satisfiable. Reads a FormulaTree object and returns a Boolean."
    atoms = tree.atoms()
    assign = {a : False for a in atoms}
    if evaluate(tree, assign) : return True
    while False in assign.values() :
        assign = nextAssignment(assign)
        if evaluate(tree, assign): return True
    return False

class Tree(object):
    """Basic binary tree class"""
    def __init__(self, node, left = None, right = None):
        self.node = node
        self.left = left
        self.right = right
        return
    
    def __iter__(self):
        self.back = [self]
        return self
    
    def __next__(self):
        if self.back == []:
            raise StopIteration
        node = self.back[0].node
        if self.back[0].left != None:
            self.back += [self.back[0].left]
        if self.back[0].right != None:
            self.back += [self.back[0].right]
        self.back = self.back[1:]
        return node
    
    def show(self):
        "Prints every node of the tree"
        for node in self:
            print(node)
        return

def initial_segment(expr, init_set):
    for init_seg in init_set:
        cx = 0
        if len(init_seg) > len(expr):
            continue
        for n in range(len(init_seg)):
            if init_seg[n] == expr[n]:
                cx += 1
        if cx == len(init_seg):
            return init_seg
    return None

class FormulaTree(Tree):
    "A syntactic tree of a sentential formula"
    def __init__(self, formula, unary, binary):
        # Reads a formula, a set of unary connectives and a set of binary connectives, and returns the syntax tree of the formula
        self.node = None
        self.left = None
        self.right = None

        formula = formula.replace(' ', '')

        if formula != '':
            if len(formula) == 1:
                if formula[0] >= 'a' and formula[0] <= 'z' and formula[0] != 'v':
                    self.node = formula[0]
                return
                # Exception: não é uma fórmula (não é uma variável sentencial válida)
            
            if formula[0] != '(':
                return
                # Exception: não é uma fórmula (parênteses errados?)
            
            if formula[1] in unary:
                if formula[-1] != ')':
                    return
                    # Exception: não é uma fórmula (parênteses errados?)
                self.node = formula[1]
                self.left = FormulaTree(formula[2:-1], unary, binary)
                return
            
            lp = 0
            rp = 0
            cx = 1
            if formula[cx] == '(':
                lp += 1
            elif formula[cx] == ')':
                rp += 1
            cx += 1
            while lp != rp:
                if cx >= len(formula):
                    return
                    # Exception: não é uma fórmula (número de abre parênteses diferente de fecha parênteses)
                elif formula[cx] == '(':
                    lp += 1
                elif formula[cx] == ')':
                    rp += 1
                cx += 1
            
            connective = initial_segment(formula[cx:], binary)
            if connective == None:
                return
                # Exception: não é uma fórmula (não é um conectivo sentencial válido)
            
            self.node = connective
            self.left = FormulaTree(formula[1:cx], unary, binary)
            self.right = FormulaTree(formula[cx+len(connective):-1], unary, binary)

        return

    def polish(self):
        "Returns the formula in polish notation"
        pformula = self.node
        if self.left != None : pformula += self.left.polish()
        if self.right != None : pformula += self.right.polish()
        return pformula

    def common(self):
        "Returns the formula in common notation"
        if self.left == None : formula = self.node
        elif self.right == None : formula = '(' + self.node + self.left.common() + ')'
        else : formula = '(' + self.left.common() + self.node + self.right.common() + ')'
        return formula

    def atoms(self):
        "Returns the set of atomic formulas that occurs in the formula"
        if self.left == None : latoms = {self.node}
        elif self.right == None : latoms = self.left.atoms()
        else : latoms = self.left.atoms() | self.right.atoms()
        return latoms

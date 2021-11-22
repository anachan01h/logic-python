import logic

formula = input("Write a formula: ")
ftree = logic.FormulaTree(formula, logic.UNARY, logic.BINARY)
if None not in ftree:
    print("It's a formula! :)")
    print("It's polish notation is: {}".format(ftree.polish()))
    if logic.isValid(ftree):
        print("This formula is valid! :)")
    else:
        print("This formula isn't valid! :(")
    if logic.isSatisfiable(ftree):
        print("This formula is satisfiable! :)")
    else:
        print("This formula isn't satisfiable! :(")
else:
    print("It's not a formula! :(")
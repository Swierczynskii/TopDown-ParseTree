##Checker
def checkFirst(char):
    if char != "S":
        print("\nError: CFG should start with capital letter 'S'", "\n")
        return True
    return False

##Checker
def checkLineFirst(char):
    if char.isupper():
        return False
    else:
        print("\nError: CFG should have non terminal (capital) letters",
        "\nat the beginning of each line",
        "\n")
        return True

## Checker
def arrowCheck(line):
    if line[1] != " ":
        print("\nError: CFG has to be written in a specific syntax,",
        "\nNon terminal symbol, space, arrow, space, (non)terminal symbols.",
        "\nExample: 'S -> a1|vBs|1'",
        "\n")
        return True
    if line[2] != "-":
        print("\nError: CFG has to be written in a specific syntax,",
        "\nNon terminal symbol, space, arrow, space, (non)terminal symbols.",
        "\nExample: 'S -> a1|vBs|1'",
        "\n")
        return True
    if line[3] != ">":
        print("\nError: CFG has to be written in a specific syntax,",
        "\nNon terminal symbol, space, arrow, space, (non)terminal symbols.",
        "\nExample: 'S -> a1|vBs|1'",
        "\n")
        return True 
    if line[4] != " ":
        print("\nError: CFG has to be written in a specific syntax,",
        "\nNon terminal symbol, space, arrow, space, (non)terminal symbols.",
        "\nExample: 'S -> a1|vBs|1'",
        "\n")
        return True 
    return False

## Checker
def checkString(str_):
    if str_ == "$":
        return str_

    for ch in str_:
        if ch == "$":
            if len(str_) > 1:
                print("\nError: Given string cannot contain special character '$'",
                "\ntogether with any other characters.",
                "\n")
                return False
        if ch.isupper():
            print("\nError: Given string cannot contain capital letters\n")
            return False
    return True

## Checker
def spaceCounter(num):
    if num > 2:
        print("\nError: spaces in file should be only next to an arrow ('->'),", 
        "\none to the left and one to the right.",
        "\n")
        return True
    return False

## Checker
def ifRepeat(nonTerminals):
    for ch in nonTerminals:
        j = 0
        for ch2 in nonTerminals:
            if ch == ch2:
                j += 1
        if j > 1:
            print("\nError: There are some repetitions of non-terminal values in CFG.\n")
            return True
    return False

## Checker
def isConnected(nonTerminals, nTermValue):
    for term in nonTerminals:
        i = 0
        for value in nTermValue:
            for ch in value:
                if term == ch:
                    i += 1
        if term != 'S' and i == 0:
            print("\nError: There is at least one non-terminal value in CFG",
            "\nwhich is not defined in any rules of production\n")
            return True
    
    for value in nTermValue:
        for ch in value:
            i = 0
            if ch.isupper():
                for term in nonTerminals:
                    if ch == term:
                        i += 1
                if i == 0:
                    print("\nError: There is at least one non-terminal value in CFG",
                    "\nwhich has not its rules of production defined\n")
                    return True
                    
    return False
import Checker as check
from PTree import ParseTree
## Parser
def readFile(filename):  
    f = open(filename, 'r')

    filestr = ""
    nTermValue = []
    nonTerminals = []

    for line in f:

        toCheck = line.rstrip('\n')
        filestr += line
        nonTerminals.append(toCheck[0]) # non terminals list

        if check.checkLineFirst(toCheck[0]): # check if non-terminals are uppercased
            return None 

        value = ""
        space_counter = 0
        index = 0

        if check.arrowCheck(line): # check if arrow after non-terminal is written correctly
            return None

        for ch in line:     
            if ch == '\n':
                break     
            if index > 4:
                if ch is line[index]:
                    value += ch
            if ch == " ":
                space_counter += 1
            if check.spaceCounter(space_counter): # there should be only 2 spaces
                return None
            index += 1

        nTermValue.append(value)    # non terminal values

    NonTerminalDic = {}

    if check.checkFirst(filestr[0]): # check is files starts with "S"
        return None

    if check.ifRepeat(nonTerminals): # check if non-terminals repeats themselves
        return None

    if check.isConnected(nonTerminals, nTermValue): # check if non-terminals are connected
        return None                                 # the nodes in the tree must be connected

    if len(nonTerminals) == len(nTermValue):
        i = 0
        for key in nonTerminals:
            value = nTermValue[i].split(sep="|")
            NonTerminalDic[key]= value
            i += 1
    else:
        print("\nError: Something went wrong :(", "\n")
        return None

    return NonTerminalDic

## Parser
def parse(filename, str_):

    NonTerminalDic = readFile(filename)
    
    if NonTerminalDic == None:
        return Exception

    if check.checkString(str_):
        inputStr = str_
    else:
        return Exception
    tree = ParseTree()
    tree.addRoot(list(NonTerminalDic.keys())[0], NonTerminalDic[list(NonTerminalDic.keys())[0]][0], None)
    tree.printTree()

      #tree.createTree(dictionary, root, 'read', string_index, kids_index) 
    if tree.createTree(NonTerminalDic, tree.nodes[0], inputStr, 0, 0) == None:
        return Exception
    
    return





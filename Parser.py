import Checker as check

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

        if check.checkLineFirst(toCheck[0]):
            return None 

        value = ""
        space_counter = 0
        index = 0

        if check.arrowCheck(line):
            return None

        for ch in line:     
            if ch == '\n':
                break     
            if index > 4:
                if ch is line[index]:
                    value += ch
            if ch == " ":
                space_counter += 1
            if check.spaceCounter(space_counter):
                return None
            index += 1

        nTermValue.append(value)    # non terminal values

    NonTerminalDic = {}

    if check.checkFirst(filestr[0]):
        return None

    if check.ifRepeat(nonTerminals):
        return None

    if check.isConnected(nonTerminals, nTermValue):
        return None

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

    print(NonTerminalDic, inputStr)
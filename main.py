import Checker as check

##Printer
def helper():
    print("helper - write text how to use program")

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
            return Exception 

        value = ""
        space_counter = 0
        index = 0

        if check.arrowCheck(line):
            return Exception

        for ch in line:     
            if ch == '\n':
                break     
            if index > 4:
                if ch is line[index]:
                    value += ch
            if ch == " ":
                space_counter += 1
            if check.spaceCounter(space_counter):
                return Exception
            index += 1

        nTermValue.append(value)    # non terminal values

    NonTerminalDic = {}

    if check.checkFirst(filestr[0]):
        return Exception

    if len(nonTerminals) == len(nTermValue):
        i = 0
        for key in nonTerminals:
            value = nTermValue[i].split(sep="|")
            NonTerminalDic[key]= value
            i += 1
    else
        print("\nError: Something went wrong, sorry", "\n")
        return Exception
        
    print(NonTerminalDic)

def main():
    helper()
    filename = 'input.txt'
    #str_ = input("Give me the word to check:")
    str_ = "read"

    try:
        check.checkString(str_)
        readFile(filename)
    except Exception:
        return



if __name__ == '__main__':
    main()
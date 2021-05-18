import Parser as p

##Printer
def helper():
    print("helper - write text how to use program")

def readInput():
    filename = 'input.txt'
    #str_ = input("Give me the word to check:")
    str_ = "read"
    return filename, str_

def main():
    
    #helper()
    try:
        filename, str_ = readInput()
        p.parse(filename, str_)
    except Exception:
        return



if __name__ == '__main__':
    main()
import Parser as p
import Tests as t


def readInput():
    filename = input("\nGive the file name: ")
    str_ = input("\nGive the string to be checked: ")
    return filename, str_

def main(): # In order to use written test, user needs to call a chosen test method in marked place
    try: 
        filename, str_ = readInput() # Call here chosen test method
        p.parse(filename, str_)
    except Exception:
        return

if __name__ == '__main__':
    main()
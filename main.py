import Parser as p
import Tests as t


def readInput():
    filename = input("\nGive the file name: ")
    str_ = input("\nGive the string to be checked: ")
    return filename, str_

def program():
    print("\n______Program_______\n")
    filename, str_ = readInput() # Call here chosen test method
    p.parse(filename, str_)

def tests():
    print("\n______TEST1_______\n")
    filename, str_ = t.test1()
    p.parse(filename, str_)
    print("\n______TEST2_______\n")
    filename, str_ = t.test2()
    p.parse(filename, str_)
    print("\n______TEST3_______\n")
    filename, str_ = t.test3()
    p.parse(filename, str_)
    print("\n______TEST4_______\n")
    filename, str_ = t.test4()
    p.parse(filename, str_)
    print("\n______TEST5_______\n")
    filename, str_ = t.test5()
    p.parse(filename, str_)
    print("\n______TEST6_______\n")
    filename, str_ = t.test6()
    p.parse(filename, str_)
    print("\n______TEST7_______\n")
    filename, str_ = t.test7()
    p.parse(filename, str_)
    
def main(): # User needs to uncomment program() function and comment tests() function in order to use program for his/her purposes
    
    try: 
        tests()
        #program()
    except Exception:
        return

if __name__ == '__main__':
    main()
from Node import TreeNode

class ParseTree:

    def __init__(self):
        self.nodes = []

    def addNode(self, nonTerm, children, parent):
        self.nodes.append(TreeNode(nonTerm, children, parent))

    def addRoot(self, nonTerm, children, parent):
        if not self.nodes:
            self.nodes.append(TreeNode(nonTerm, children, parent))
        else:
            return False

    def removeNode(self, val):
        for n in self.nodes:
            if(n.value == val):
                self.nodes.remove(n)
    
    def printTree(self):
        print("====================")
        for node in self.nodes:
            print(node)
        print("====================")

    def findByValue(self, value):
        for node in self.nodes:
            if node.value == value:
                return node

    def findNodesIndex(self, value):
        index = 0
        for node in self.nodes:
            if node.value == value:
                return index
            index += 1

    def editNode(self, value, kidsIndex, NonTerminalDic, parent):
        kidsIndex+=1
        for key in NonTerminalDic.keys():
            if key == value:
                if kidsIndex >= len(NonTerminalDic[key]):
                    print("\nDeleting node:",value, "\n")
                    self.removeNode(value)
                    print("\nYet another backtracking...\n")
                    prnt = self.findByValue(parent)
                    if value == 'S':
                        return None
                    return self.editNode(prnt.value, 0, NonTerminalDic, prnt.parent)
                else:
                    next_rules = NonTerminalDic[key][kidsIndex]

        print("\nDeleting node:", value, "\n")
        self.removeNode(value)
        self.addNode(value, next_rules, parent)
        new_node = self.nodes[self.findNodesIndex(value)]
        return new_node


    def createTree(self, NonTerminalDic, root, inputStr, index, kidsIndex):
        for child in root.children:
            if child.isupper():
                for key in NonTerminalDic.keys():
                    if child == key:
                        self.addNode(child, NonTerminalDic[key][0], root.value) #most left rule of production
                        self.printTree()
                        index = self.createTree(NonTerminalDic, self.findByValue(child), inputStr, index, 0)
            else:
                if child == inputStr[index]:
                    self.addNode(child, None, root.value)
                    self.printTree()
                    index+=1
                    if index == len(inputStr):
                        for node in self.nodes:
                            if node.value.isupper():
                                pass
                            else:
                                print(node)
                        break
                elif child == '$':
                    if len(root.children) == 1 and index != len(inputStr):
                        print("\nBacktracking...\n")
                        new_root = self.editNode(root.value, kidsIndex, NonTerminalDic, root.parent)
                        self.printTree()
                        index = self.createTree(NonTerminalDic, new_root, inputStr, index, kidsIndex+1)
                else:
                    print("\nChild for which we need backtracking:",child)
                    print("Backtracking...\n")
                    new_root = self.editNode(root.value, kidsIndex, NonTerminalDic, root.parent)
                    if new_root == None:
                        break
                    self.printTree()
                    index = self.createTree(NonTerminalDic, new_root, inputStr, index, kidsIndex+1)
                    if len(root.children) != 1:
                        break 
        return index
                        



from Node import TreeNode

class ParseTree:

    def __init__(self):
        self.nodes = []

    def addNode(self, nonTerm, children, parents):
        self.nodes.append(TreeNode(nonTerm, parents, children))

    def removeNode(self, nonTerm):
        for n in self.nodes:
            if(n.nonTerminalChar == nonTerm):
                self.nodes.remove(n)
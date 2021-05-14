
class TreeNode:

    def __init__(self, nonTerminalChar, parents, children):
        self.nonTerminalChar = nonTerminalChar
        self.terminalChar = children
        self.parents = parents
    
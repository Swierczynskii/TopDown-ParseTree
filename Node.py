
class TreeNode:

    def __init__(self, value, children, parent):
        self.value = value
        self.children = children
        self.parent = parent
    
    def __repr__(self):
        if self.value.isupper():
            return f'Non-terminal Node: {self.value}\nwith children: {self.children}\n'
        else:
            return f'Terminal Node: {self.value}\n'
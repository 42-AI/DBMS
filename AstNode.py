class AstNode:
    def __init__(self, data=None, right=None, left=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        if self.left and self.right:
            return self.left.__str__() + self.right.__str__() + f"[{self.data}]"
        elif self.left:
            return self.left.__str__() + f"[{self.data}]"
        elif self.right:
            return self.right.__str__() + f"[{self.data}]"
        else:
            return f"[{self.data}]"
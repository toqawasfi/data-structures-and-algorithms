class TreeNode():
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
    
    def insert(self,value):
        if value<self.value :
            if self.left is None:
                self.left=TreeNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right=TreeNode(value)
            else:
                self.right.insert(value)

    def in_order(node):
        if node:
            in_order(node.left)
            print(node.value)
            in_order(node.right)

        # if self.left:
        #     self.left.in_order()
        # print(self.value)
        # if self.right:
        #      self.right.in_order()

tree=TreeNode(50)
tree.insert(5)
tree.insert(6)
tree.insert(10)
tree.insert(222)
tree.insert(70)
tree.in_order()

node.left=node
# self.left=node
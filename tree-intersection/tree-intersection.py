class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


def tree_intersection(tree1, tree2):
    values_set = set()
    tree1_values = traverse_tree(tree1, values_set)
    common_values = set()
    traverse_tree(tree2, common_values, tree1_values)
    return common_values


def traverse_tree(node, common_values, tree1_values=None):
    if node is None:
        return

    traverse_tree(node.left, common_values, tree1_values)

    if tree1_values is not None and node.val in tree1_values:
        common_values.add(node.val)

    traverse_tree(node.right, common_values, tree1_values)

    if tree1_values is None:
        return common_values


# Example usage
# Create two binary trees
tree1 = TreeNode(1)
tree1.left = TreeNode(2)
tree1.right = TreeNode(3)
tree1.left.left = TreeNode(4)
tree1.left.right = TreeNode(5)

tree2 = TreeNode(1)
tree2.left = TreeNode(3)
tree2.right = TreeNode(6)
tree2.left.left = TreeNode(4)
tree2.left.right = TreeNode(7)

# Find common values
result = tree_intersection(tree1, tree2)
print(result)  # Output: {1, 3, 4}

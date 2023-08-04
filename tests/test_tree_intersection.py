import pytest
from tree_intersection.tree_intersection import tree_intersection
# Define the TreeNode class for binary tree nodes
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Binary tree 1
tree1 = TreeNode(1)
tree1.left = TreeNode(2)
tree1.right = TreeNode(3)
tree1.left.left = TreeNode(4)
tree1.left.right = TreeNode(5)

# Binary tree 2
tree2 = TreeNode(3)
tree2.left = TreeNode(4)
tree2.right = TreeNode(6)
tree2.left.left = TreeNode(1)
tree2.left.right = TreeNode(7)

# Test cases for tree_intersection function
@pytest.mark.parametrize("tree1, tree2, expected", [
    (tree1, tree2, {1, 3, 4}),
    (tree1, None, set()),
    (None, tree2, set()),
    (None, None, set()),
    (TreeNode(1), TreeNode(1), {1}),
    (TreeNode(1), TreeNode(2), set())
])
def test_tree_intersection(tree1, tree2, expected):
    result = tree_intersection(tree1, tree2)
    assert result == expected
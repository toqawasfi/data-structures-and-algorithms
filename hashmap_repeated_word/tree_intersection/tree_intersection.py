class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def tree_intersection(tree1, tree2):
    def build_hashmap(node, hashmap):
        if node:
            hashmap[node.value] = True
            build_hashmap(node.left, hashmap)
            build_hashmap(node.right, hashmap)

    def find_intersection(node, hashmap, intersection):
        if node:
            if node.value in hashmap:
                intersection.add(node.value)
            find_intersection(node.left, hashmap, intersection)
            find_intersection(node.right, hashmap, intersection)

    # Step 1: Traverse the first binary tree and store its values in a hashmap
    hashmap = {}
    build_hashmap(tree1, hashmap)

    # Step 2 & 3: Traverse the second binary tree and find the intersection of values
    intersection = set()
    find_intersection(tree2, hashmap, intersection)

    # Step 4: Return the set containing the intersection of values
    return intersection
# Example binary trees
# Tree 1
tree1 = TreeNode(1)
tree1.left = TreeNode(2)
tree1.right = TreeNode(3)
tree1.left.left = TreeNode(4)

# Tree 2
tree2 = TreeNode(3)
tree2.left = TreeNode(4)
tree2.right = TreeNode(5)
tree2.left.left = TreeNode(6)

result = tree_intersection(tree1, tree2)
print(result)  # Output: {3, 4} (the intersection of values in both trees)

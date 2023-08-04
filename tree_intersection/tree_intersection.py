from Hash_table.hash import Hashtable
def tree_intersection(tree1, tree2):
    # Create a Hashtable to store values from tree1
    hashtable = Hashtable()

    # Traverse tree1 and store all values in the hashtable
    def traverse_and_store(node):
        if node is None:
            return
        hashtable.set(node.value, True)
        traverse_and_store(node.left)
        traverse_and_store(node.right)

    traverse_and_store(tree1)

    # Traverse tree2 and check if each value is present in the hashtable
    def traverse_and_check(node, result):
        if node is None:
            return
        if hashtable.has(node.value):
            result.add(node.value)
        traverse_and_check(node.left, result)
        traverse_and_check(node.right, result)

    # Create a set to store the common values
    common_values = set()

    traverse_and_check(tree2, common_values)

    return common_values
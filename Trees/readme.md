# Challenge Title
CC15: Binary Tree and BST Implementation

## Whiteboard Process
<!-- Embedded whiteboard image -->
[CC15](./CC15.jpg)

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
ISearch (Contains): O(log n) time complexity on average, where n is the number of nodes in the tree. In the worst case (unbalanced tree), the time complexity can be O(n).

Insertion (Add): O(log n) time complexity on average, where n is the number of nodes in the tree. In the worst case (unbalanced tree), the time complexity can be O(n) due to the tree becoming skewed.

Deletion: O(log n) time complexity on average, where n is the number of nodes in the tree. In the worst case (unbalanced tree), the time complexity can be O(n).

Traversal (In-order, Pre-order, Post-order): O(n) time complexity, where n is the number of nodes in the tree. This is because we need to visit every node in the tree.
## Solution
<!-- Show how to run your code, and examples of it in action -->
To run the code you have to pass an array and vlue to be inserted ,write the following commands on CLI:
to test code:
pytest
to run code :
python file_path.

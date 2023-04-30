# Challenge Title
CC7: linked_list_kth

## Whiteboard Process
<!-- Embedded whiteboard image -->
[cc7](./cc7.jpg)

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
Start at the head of the linked list.
Traverse the list to find the length of the list. At the end of this traversal, we know the total number of nodes in the list, which is n.
Calculate the distance from the beginning of the list to the kth node from the end, which is (n-k).
Start at the head of the list again.
Traverse the list (n-k) nodes from the beginning. At the end of this traversal, we have reached the kth node from the end.
Return the value of the kth node from the end.
Time complexoty:O(n)
Space complexity :O(1)

## Solution
<!-- Show how to run your code, and examples of it in action -->
To run the code you have to pass an array and vlue to be inserted ,write the following commands on CLI:
to test code:
pytest
to run code :
python file_path.

my PR:

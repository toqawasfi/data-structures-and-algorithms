## Title
CC8: linked_list_zip
## Whiteboard Process
<!-- Embedded whiteboard image -->
[linked_list_zip](./ziplist.jpg)

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
The Time complexity for zip_lists function in the current implementation is O(n), where n is the length of the smaller linked list between l1 and l2. 
The space complexity is O(1)

Approach:Check if either of the linked lists l1 or l2 is empty. If one of them is empty, return the other linked list as is.
Set the head of l1 as the starting point of the new linked list.
While there are still nodes in both l1 and l2, do the following: a. Save the next node of l1 and l2 in separate variables. b. Set the next node of the current node of l1 as the head of the current node of l2. c. Set the next node of the current node of l2 as the saved next node of l1. d. Move the current node pointers of l1 and l2 to their respective next nodes.
Return the head of the new linked list.


## Solution
<!-- Show how to run your code, and examples of it in action -->
To run the code you have to pass two .


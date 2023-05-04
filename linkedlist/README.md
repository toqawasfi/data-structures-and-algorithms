## Title
CC5: linked_list
## Whiteboard Process
<!-- Embedded whiteboard image -->
[linked_list](./CC5.jpg)

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
The Time complexity for zip_lists function in the current implementation is O(n), where n is the length of the smaller linked list between l1 and l2. 
The space complexity is O(1)

Approach:Define the Node class with an __init__ method that takes a value argument and initializes the value and next attributes.

Define the LinkedList class with an __init__ method that initializes the head attribute to None.

Define the __str__ method for the LinkedList class. Initialize a variable called output to an empty string. Set a variable current to self.head. Use a while loop to iterate through the linked list, appending the value of each node to output followed by an arrow symbol. Update current to the next node in the list at each iteration. Finally, append the string "Null" to output to indicate the end of the list, and return output.

Define the __repr__ method for the LinkedList class. Initialize an empty list called nodes. Set a variable current to self.head. Use a while loop to iterate through the linked list, appending the string representation of each node's value to nodes. Update current to the next node in the list at each iteration. 

Define the insert method for the LinkedList class. Create a new Node instance with the given value and assign it to a variable called node. Set a variable current to self.head. Set self.head to node. Set node.next to current.

Define the includes method for the LinkedList class that takes a value argument. Set a variable current to self.head. Use a while loop to iterate through the linked list. If the value of the current node is equal to the given value, return True. Update current to the next node in the list at each iteration. If the end of the list is reached without finding the value, return False.
## Solution
<!-- Show how to run your code, and examples of it in action -->
To run the code you have to pass two .


# Challenge Title
CC26: insertion sort

## Whiteboard Process
<!-- Embedded whiteboard image -->
[CC26](./CC26.jpg)

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
Start with the second element and iterate through the array.
Compare the current element with the elements on its left.
If a larger element is found, shift it one position to the right.
Repeat step 3 until the correct position for the current element is found.
Insert the current element into its correct position.
Repeat steps 2 to 5 for all elements in the array.
The array is now sorted in ascending order.
Time complexity :O(n^2)
Space complexity:O(n1)
## Solution
<!-- Show how to run your code, and examples of it in action -->
To run the code you have to pass an array and vlue to be inserted ,write the following commands on CLI:
to test code:
pytest
to run code :
python file_path.



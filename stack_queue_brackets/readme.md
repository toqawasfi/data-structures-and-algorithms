# Challenge Title
CC13: stack-queue-brackets

## Whiteboard Process
<!-- Embedded whiteboard image -->
[cc13](./CC13.jpg)

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
Initialize an empty stack to keep track of opening brackets.
Iterate through each character in the input string.
If the character is an opening bracket (i.e., one of (, [, or {), push it onto the stack.
If the character is a closing bracket (i.e., one of ), ], or }), do the following:
Check if the stack is empty. If it is, return False since there is no matching opening bracket.
Pop the topmost opening bracket from the stack.
Check if the opening bracket matches the closing bracket in terms of type (i.e., ( matches ), [ matches ], and { matches }). If they don't match, return False.
After iterating through all characters, check if the stack is empty. If it is, return True as all opening brackets have been properly closed. If the stack is not empty, return False since there are unmatched opening brackets.
Time complexity :O(n)
Space complexity:O(n)
## Solution
<!-- Show how to run your code, and examples of it in action -->
To run the code you have to pass an array and vlue to be inserted ,write the following commands on CLI:
to test code:
pytest
to run code :
python file_path.



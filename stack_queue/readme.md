## Title
CC: Queue and stack
## Whiteboard Process
<!-- Embedded whiteboard image -->
[Queue & Stack](./q&s.jpg)

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
The Time complexity for zip_lists function in the current implementation is O(n), where n is the length of the smaller linked list between l1 and l2. 
The space complexity is O(1)

ApproachA stack is a Last-In-First-Out (LIFO) data structure, meaning that the most recently added item is the first one to be removed. It operates by adding elements to the top of the stack and removing them from the top as well. In the implementation of the stack, push() method is used to add elements to the top of the stack while pop() method is used to remove elements from the top.

A queue, on the other hand, is a First-In-First-Out (FIFO) data structure, meaning that the first item added to the queue is the first one to be removed. It operates by adding elements to the rear of the queue and removing them from the front. In the implementation of the queue, enqueue() method is used to add elements to the rear while dequeue() method is used to remove elements from the front.

## Solution
<!-- Show how to run your code, and examples of it in action -->
To run the code you have to run this command:
python -m stack_queue.file_name

[PR](https://github.com/toqawasfi/data-structures-and-algorithms/pull/12)
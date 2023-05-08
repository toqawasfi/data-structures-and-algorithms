# Challenge Title
CC11: stack_queue psoudo
## Whiteboard Process
<!-- Embedded whiteboard image -->
[stack_queue psoudo](./cc11.jpg)

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
The time complexity of the enqueue method in the pseudo_queue class is O(n), where n is the number of elements in the queue. This is because when an element is added to the queue, all elements in my_stack1 are removed and added to my_stack2, and then the new element is added to my_stack2. This operation takes O(n) time as all elements in my_stack1 need to be removed and added to my_stack2.

The time complexity of the dequeue method in the pseudo_queue class is O(1), which is constant time. This is because the elements are dequeued from my_stack1, which has the first element of the queue at its top.

The space complexity of the pseudo_queue class is O(n), where n is the number of elements in the queue. This is because the class uses two instances of the my_stack class, each of which stores the elements of the queue. The maximum size of the queue is n, so the space complexity of the class is O(n).


## Solution
<!-- Show how to run your code, and examples of it in action -->
To run the code you have to pass an array and vlue to be inserted .
[PR](https://github.com/toqawasfi/data-structures-and-algorithms/pull/13)
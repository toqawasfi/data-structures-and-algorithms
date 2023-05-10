## Title
CC12: First-in, First out Animal Shelter.
## Whiteboard Process
<!-- Embedded whiteboard image -->
[Animal Shelter](./CC12.jpg)

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
The time complexity of the enqueue method is O(1) as it only involves appending to a list, which is a constant-time operation.

The time complexity of the dequeue method is O(n) in the worst case, where n is the number of animals in the queue. This is because the method involves a while loop that may need to iterate through all elements in the queue before finding the animal to dequeue. However, in practice, the loop will usually only need to iterate through a small number of elements, so the average case time complexity will be lower than O(n).

The space complexity of both methods is O(1) as they only use a fixed amount of memory to store the animal queues and a temporary container list.

## Solution
<!-- Show how to run your code, and examples of it in action -->
To run the code you have to run this command:
python -m stack_queue.file_name

[PR](https://github.com/toqawasfi/data-structures-and-algorithms/pull/12)
# Challenge Title
CC27: Merg sort

## Whiteboard Process
<!-- Embedded whiteboard image -->
[CC26](./CC27.jpg)

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
Divide: The input array is recursively divided into smaller sub-arrays until each sub-array contains only one element. This is done by finding the middle index of the array and recursively calling the merge sort function on the left and right halves.

Merge: Once the array is divided into single-element sub-arrays, the merging step begins. Pairs of adjacent sub-arrays are merged together to create sorted sub-arrays. This process continues until all sub-arrays are merged back together, resulting in a fully sorted array.

Comparison and Merging: During the merging process, elements from two sub-arrays are compared and placed in sorted order into a temporary array. The temporary array is then copied back to the original array, replacing the original unsorted elements with the sorted elements.

Repeat and Combine: Steps 1-3 are repeated recursively for the divided sub-arrays until the entire array is sorted. This process combines the sorted sub-arrays to eventually produce a fully sorted array.
Time complexity :O(nlog(n))
Space complexity:O(n)
## Solution
<!-- Show how to run your code, and examples of it in action -->
To run the code you have to pass an array and vlue to be inserted ,write the following commands on CLI:
to test code:
pytest
to run code :
python file_path.



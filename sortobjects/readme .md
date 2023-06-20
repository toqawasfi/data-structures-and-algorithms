
# Challenge Title
CC28: Sorting: Comparisons


## Approach & Efficiency
movies_sorted_by_year: This method sorts movies by year in descending order. It takes a list of movie objects as input and returns an ordered list of objects based on the most recent years.

movies_sorted_by_title: This method sorts movies by title while ignoring leading "A"s, "An"s, or "The"s. It takes a list of movie objects as input and returns an ordered list of objects based on alphabetical order, ignoring the specified prefixes.

The code also includes a sample list of movie objects movies_set, and an instance of the Movies class called my_sort is created. The two methods are invoked on my_sort to demonstrate their functionality.

The space complexity of both methods is O(1) since they do not use any additional data structures that grow with the input size. They perform in-place sorting using the sorted function.
Time Complexity:

movies_sorted_by_year: The time complexity of this method is O(n log n) due to the sorting operation using the sorted function. Here, 'n' represents the number of movie objects in the input list.

movies_sorted_by_title: The time complexity of this method is also O(n log n) due to the sorting operation using the sorted function. Additionally, there is a regular expression substitution that runs on each title, but its complexity is relatively low compared to the sorting operation.

## Solution
<!-- Show how to run your code, and examples of it in action -->
To run the code you have to pass an array and vlue to be inserted ,write the following commands on CLI:
to test code:
pytest
to run code :
python file_path.

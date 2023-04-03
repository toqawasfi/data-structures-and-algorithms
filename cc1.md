## Problem Domain
Write a function called reverseArray which takes an array as an argument. Without utilizing any of the built-in methods available to your language, return an array with elements in reversed order.

## visulization:
its drawn in the whiteboard ,where the array elements will be reversed

## Approach
1. Create a method to reverse array
2. Iterate through an array
3. return reversed array

 ## Big O (Efficiency)
 - The Time complexity is O(n),because we have one for loop
 - The space complexity of this code is also O(n). This is because we create a new list reversed_arr of size n to store the reversed elements of the input array.

 ## Pseudocode:
reverseArray(arr):
    reversedArray = empty list
    for i from length of arr - 1 to 0, decrement by 1:
        append arr[i] to reversedArray
    print reversedArray
    return reversedArray

arr1 = [1, 2, 3, 4, 5]
reverseArray(arr1)

## The Code:

def reverseArray(arr):
    reversedArray=[]
    for i in range(len(arr)-1,-1,-1):
         reversedArray.append(arr[i])

    print(reversedArray)
    return reversedArray
    

## img
   |Whiteboard                | [WhiteBoard](./whiteboard1.jpg)

## summary : i wrote code that reverse array.
## Discription : using python language i reversed an arry element using for loop to iterate over the indecies.

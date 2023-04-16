def binarysearch(arr,key):
  '''
  Binary search is a function takes two parameters list and key
  it returns the index of the key inside of arr

  '''
  first= 0
  last=len(arr)-1

  while last>=first :
     mid =(first+last) // 2
     
     if arr[mid] == key :
      
      return mid
    
     elif arr[mid]<key :
       first=mid +1
      
      
     
     elif arr[mid]>key :
       last= mid -1
       
       
  return -1
     
print(binarysearch([4, 8, 15, 16, 23, 42], 15))
print(binarysearch([-131, -82, 0, 27, 42, 68, 179], 42))
print(binarysearch([11, 22, 33, 44, 55, 66, 77], 90))
print(binarysearch([1, 2, 3, 5, 6, 7], 4))

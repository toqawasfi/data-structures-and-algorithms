def binarysearch(arr,key):
  first= 0
  last=len(arr)-1
  while last>=first :
     mid =(first+last) // 2
    #  print(mid)
     if arr[mid] == key :
      print ( mid)
      return mid
    
     elif arr[mid]<key :
       first=mid +1
       if arr[first ]== key:
        print (first)
        return first
      
     
     elif arr[mid]>key :
       last= mid -1
       if arr[last ]== key:
         print(last)
         return last
       
  return -1
     
       
    
      

    

binarysearch([2,4,6,8,10,12],11)
binarysearch([1,2,3,4,5,6,7],7)
# binarysearch([4, 8, 15, 16, 23, 42], 15)
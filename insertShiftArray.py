def insertShiftArray(arr, value):
    '''
    This function responsible for inserting an element to array using append method
    arr: it takes array and the value to be inserted
    Return: it returns an array with the new value

    '''
    length = len(arr)
    midlle =  length // 2

    result = []

  
    if length %2==0:
     for i in range(len(arr)):
        if i == midlle:
            result.append(value)
          
        result.append(arr[i])
     print(result)
     return result
    
    if length %2!=0:
     for i in range(len(arr)):
      
        if i == (midlle+1):
            result.append(value)
        
        result.append(arr[i])
     print(result)
     return result
    
   




####Stretch Goal####

def delete(arr, value):
    midlle = len(arr) // 2
    result = []

    for i in range(len(arr)):
      
        if i == midlle:
            result.append(value)
     
        elif i !=midlle and i < midlle:
            result.append(arr[i])
        elif i != midlle and i > midlle:
            result.append(arr[i-1])
    print (result)
    return result

delete([10,20,30,40],50)
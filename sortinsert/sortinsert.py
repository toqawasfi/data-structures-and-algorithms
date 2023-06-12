def insertsort(arr,value):
    arr.append(value)
    length=len(arr)
    for i in range(1,length):
        key=arr[i]
        j=i-1
        while(j>=0 and arr[j]>key):
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=key
    return arr

print(insertsort([20,18,12,8,5,-2],3))
print(insertsort([5,12,7,5,5,7],3))
print(insertsort([2,3,5,7,13,11],3))



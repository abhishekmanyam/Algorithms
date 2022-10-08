
from bisect import bisect_left
list = []

def find(arr,x,k):
    global list
    position = bisect_left(arr, x)
    i = position -1
    j = position 

    while i >=0 and j <= len(arr)-1 and k > 0:
        if x - arr[i] <= arr[j] - x :
            list.insert(0,arr[i])
            k+=-1
            i+=-1
        else : 
            list.append(arr[j])
            k+=-1
            j+=1
    while k > 0 and i >=0 :
        list.insert(0,arr[i])
        i+=-1
        k+=-1
    while k > 0 and j < len(arr) :
        list.append(arr[j])
        j+=1
        k+=-1
    return list

print(find([1,2,3,4,4,7], 6.5, 3))


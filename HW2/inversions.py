
inversions = 0
def merge(left,right,arr):
    global inversions
    i = 0
    j = 0
    index = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[index] = left[i]
            index +=1
            i +=1
        else :
            arr[index] = right[j]
            index +=1
            j +=1
            
            inversions += len(left[i:])
    while i < len(left):
        arr[index] = left[i]
        index +=1
        i+=1
        
    while j <len(right):
        arr[index] = right[j]
        index +=1
        j+=1
    return arr , inversions


def mergesort(arr):
    if len(arr) > 1:
        mid = len(arr)//2

        left = arr[:mid]
        right = arr[mid:]
        mergesort(left)
        mergesort(right)

        return merge(left,right,arr)
        
    else:
        return 0

def num_inversions(arr):
    arr , k = mergesort(arr)
    return k

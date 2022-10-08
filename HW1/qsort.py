from random import randint
sort = []
def _search(arr,k):
    for x in arr:
        if isinstance(x, list):
            rand,p = _search(x,k)
            if rand == True :
                return True , x
        elif x == k :
            return True , x

    return False, arr

def search(arr,k):
    l , aray = _search(arr,k)
    return l


def sorted(arr):
    global sorted
    for x in arr:
        if isinstance(x,list):
            sorted(x)
        else :
            sort.append(x)
    return sort

def sort(arr):
    if arr == []:
        return None
    else:
        pivot = arr[0]
        left = [x for x in arr if x < pivot]
        right = [x for x in arr if x > pivot]
        return  [sort(left)] + [pivot] + [sort(right)]

print(sort([4,2,3,5,1]))





        
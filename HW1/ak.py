def qsort(array):

    match array : 
        case [] :
            return []
        case default :
            pivot = array[0]
            left = [x for x in array if x < pivot]
            right = [x for x in array if x > pivot]
            return  [qsort(left)] + [pivot] + [qsort(right)]

            

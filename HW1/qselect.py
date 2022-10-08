
from random import randint

def qselect(k,givenarr): #taking 2 aurguments (1. kth smallest value 2. List from which kth smallest number is needed)
    if len(givenarr)>0:
        rand = randint(0,len(givenarr)-1)    #generating random digit from 0 - lenght of the array. for index values of the list)
        givenarr[rand],givenarr[0] = givenarr[0],givenarr[rand] # swaping the random number with the first element. which is usefull for eliminating the pivot element which will be stored in the first index
        pivot = givenarr[0] #taking the first element as pivot
        left = [x for x in givenarr if x < pivot] # taking all the values from the list which are less than the pivot to a seperate list
        right = [x for x in givenarr[1:] if x >= pivot] # taking all the values from the list which are greater than the pivot to a seperatre list 
        givenarr = left + [pivot] + right 
        if len(left)+1 == k:   #checking if the index of the pivot is kth element as all the elements to the left are already smaller than the pivot.
            return pivot
        elif (k < len(left)+1): #we need to parse the left side of the list as kth element is located before the pivot.
            return qselect(k,left)
        else : 
            return qselect(k - (len(left)+1),right) #with parsing the right list to the pivot we need to change the value of K because we are eliminating the left list along with the pivot.
    else :
        return 0


    
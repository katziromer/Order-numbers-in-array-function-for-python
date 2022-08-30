def order(*arr):  
    arr = list(arr) #making the values within the array changeable by converting it from tuple to a list.
    lastIndex = len(arr) - 1 #defining the index of the last variable in the list.
    while lastIndex > 0: #the loop will run only until the last index will be 0.
        maximum = arr[0] #giving a starting point to the maximum.it will be initialized in any uteration.
        for num in arr: #a loop which will find us the maximum in any uteration.
                if num >= maximum and arr.index(num)<=lastIndex:#the condition for being the maximum of the uteration.
                    maximum = num 
        index_helper = arr.index(maximum)#saving the index of the maximum.
        arr[index_helper] = arr[lastIndex] #putting the value of the last variable in the index of the maximum.
        arr[lastIndex] = maximum #putting thr maximum in the last index of the uteration.
        lastIndex-=1 #making the array shorter for the next round of the while loop.
    return arr #returning the ordered list as the value of the function order().
"""
the function findes the maximum of the array and puts it in the last place in the array.
then, the function will do the same thing but without considering the variable in the last index.
then, the function will do the same thing but without considering the variables in the 2 last indexes,
and so it will do again and again until it will order the entire list.
"""

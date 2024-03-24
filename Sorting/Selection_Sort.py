# Time Complexity - O(n^2)
# Space Complexity - O(1)

import time 
def Selection_Sort(lst):
    for i in range(len(lst)): # outer loop will hover throughout the list
        min = lst[i] # first element is initialized as the smallest value
        indx = i # index of first element is initialized as the smallest index
        for j in range(i+1,(len(lst))): #inner loop travels within the unsorted portion of the list and finds the smallest element among them
            if min > lst[j]: #if the first element is not the smallest it updates the value 
                min = lst[j]
                indx = j
                (lst[i], lst[indx]) = (lst[indx], lst[i]) 
    return lst

lst = [5,6,3,4,8]
start = time.time()
print(Selection_Sort(lst))
stop = time.time()
print(float(stop - start))
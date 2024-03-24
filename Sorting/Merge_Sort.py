# Time Complexity = O(nlogn)
# Space Complexity = O(n)

import time
def Divide(lst): # Divides the list into two parts 
    mid = len(lst) // 2
    left = lst[:mid]
    right = lst[mid:]
    return left, right

def Merge(left, right): 
    new = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            new.append(left[i])
            i += 1
        else:
            new.append(right[j])
            j += 1

    new += left[i:]
    new += right[j:]
    return new

def Merge_Sort(lst):
    if len(lst) <= 1:
        return lst

    left, right = Divide(lst)

    left = Merge_Sort(left)
    right = Merge_Sort(right)

    return Merge(left, right)

lst = [5,6,3,4,8]
start = time.time()
print(Merge_Sort(lst))
stop = time.time()
print(float(stop - start))



    

            
            
            
    

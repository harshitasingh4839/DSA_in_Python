# Av. Time Complexity = O(nlogn) but worst case TC is O(n^2)
# Space Complexity = O(logn)
import time 
def Quick_Sort(lst):
    if len(lst) <= 1:
        return lst
    pivot = lst[0]
    left =  [x for x in lst[1:] if x < pivot]
    right = [x for x in lst[1:] if x >= pivot]
    return Quick_Sort(left) + [pivot] + Quick_Sort(right)


lst = [5,6,3,4,8]
start = time.time()
print(Quick_Sort(lst))
stop = time.time()
print(float(stop - start))

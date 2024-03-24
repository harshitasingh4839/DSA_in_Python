# Time Complexity = O(n^2)
# Space Complexity = O(1)
import time 
def Bubble_Sort(lst):
    for i in range(len(lst)):
        for j in range(len(lst) - i - 1):
            if lst[j]>lst[j+1]:
                lst[j],lst[j+1] = lst[j+1], lst[j]
    return lst

lst = [5,6,3,4,8]
start = time.time()
print(Bubble_Sort(lst))
stop = time.time()
print(float(stop - start))
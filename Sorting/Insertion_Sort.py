# Time Complexity = O(n^2)
# Space Complexity = O(1)
import time
def Insertion_Sort(lst):
    for i in range(1, len(lst)):
        val = lst[i]
        print(val)
        for j in range(0,i):
            if val < lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
            # print(lst)
    return lst

lst = [64, 34, 25, 12, 22, 11, 90]
start = time.time()
print(Insertion_Sort(lst))
stop = time.time()
print(float(stop - start))




# Time Complexity = O(logn)
# Space Complexity = O(1)

def Binary_Seach(lst,num):
    Lb = 0
    Ub = len(lst) - 1
    while lst:
        mid = (Ub + Lb)//2
        if num > lst[mid]:
            Lb = mid+1
            Ub = len(lst) - 1
        elif num < lst[mid]:
            Lb = 0
            Ub = mid - 1
        else :
            return mid

lst = [10, 20, 80, 30, 60, 50, 110, 100, 130, 170]
num = 110
print(Binary_Seach(sorted(lst),num))
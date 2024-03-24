# Time Complexity = O(n)
# Space Complexity = O(1)
def Linear_Search(lst,num):
    for i in range(len(lst)):
        if num == lst[i]:
            return i 
    return -1

lst = [10, 20, 80, 30, 60, 50, 110, 100, 130, 170]
num = 110
print(Linear_Search(lst,num))
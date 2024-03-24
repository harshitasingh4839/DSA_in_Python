arr = [20,30,25,31,40,50,39,250]

def res(arr):
    flag = 1
    for i in range(1,len(arr)-2,2):
        if arr[i] < arr[i+1] and arr[i+1] > arr[i+2]:
            print(arr[i],arr[i+1],arr[i+2])
            flag = 1

        else:
            flag = 0
            print(i)
            modify(arr[i:])
            return flag
    return flag

   
def modify(arr):
    arr[2] == arr[1] + 1
    print(arr)
print(res(arr))
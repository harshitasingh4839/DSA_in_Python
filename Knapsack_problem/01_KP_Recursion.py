def knapsack(w,val,cap,n):
    if n == 0 or cap == 0:
        return 0
    else :
        if w[n-1] > cap:
            return knapsack(w,val,cap,n-1)
        else:
            return max(val[n-1] + knapsack(w,val,cap - w[n-1] ,n-1), knapsack(w,val,cap,n-1))

w = [10,20,30]
val = [60,100,120]
cap = 50
n = len(w)
print(knapsack(w,val,cap,n))
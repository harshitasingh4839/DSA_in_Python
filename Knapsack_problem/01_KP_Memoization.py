def Knapsack(w, val, cap, n):
    if cap == 0 or n == 0:
        return 0
    if t[n][cap] != -1:
        print(n,cap,t[n][cap])
        return t[n][cap]

    # choice diagram
    if w[n-1] > cap:
        t[n][cap] = Knapsack(w,val,cap,n-1)
        return t[n][cap]
    else:
        t[n][cap] = max(val[n-1] + Knapsack(w,val,cap-w[n-1],n-1),Knapsack(w,val,cap,n-1))
        return t[n][cap]

w = [3,4,5,10,20,30,40,50,60]
val = [5,6,7,60,100,120,160,40,90]
cap = 100
n = len(w)

t = [[-1 for i in range(cap+1)] for j in range(n+1)]
print(Knapsack(w,val,cap,n))

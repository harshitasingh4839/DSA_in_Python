def knapsack(w, val, cap, n):
    t = [[0 for i in range(cap+1)] in range(n+1)]

    for i in range(n+1):
        for j in range(cap+1):
            if cap == 0 or n == 0:
                t[i][j] == 0
            elif w[n-1] <= cap:
                t[i][j] = max(val[i-1] + t[i-1][j - w[i-1]]),t[i-1][j]
            else:
                t[i][j] = t[i-1][j]
    return t[n][cap]


   

w = [10,20,30]
val = [60,100,120]
cap = 50
n = len(w)


print(knapsack(w,val,cap,n))
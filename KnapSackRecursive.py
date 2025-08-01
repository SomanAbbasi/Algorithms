



def Knapsack(value,weight,W,n,t):
    #Base Condition
    if n==0 or W==0:
        return 0
    #Check base Condition
    pick=0
    non_pick=0
    if weight[n-1]<=W:
        #We have Choice 1/0
        t[n][W]= max(value[n-1]+Knapsack(value,weight,W-weight[n-1],n-1,t),Knapsack(value,weight,W,n-1,t))
    else:
        t[n][W]=Knapsack(value,weight,W,n-1,t)
    return t[n][W]
    



def Solve():
    n=5
    value=[1,4,5,6,7]
    weight=[1,0,3,4,5]
    W=7
    t=[[-1 for _ in range(W+1)] for _ in range(n+1)]
    
    
    res=Knapsack(value,weight,W,n,t)
    print(res)
    
Solve()





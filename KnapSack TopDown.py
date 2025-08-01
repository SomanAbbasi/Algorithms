
def Knapsack_TopDown():
    value=[1,4,5,6,7]
    weights=[1,0,3,4,5]
    W=7
    n=5
    
    t=[[0 for _ in range(W+1)] for _ in range(n+1)]
    
    
    for i in range(1,n+1):
        for j in range(1,W+1):
            #Check if weight is less or not
            if weights[i-1]<=j:
                t[i][j]=max(value[i-1]+t[i-1][j-weights[i-1]],t[i-1][j])
            else:
                t[i][j]=t[i-1][j]
    print(t[n][W])
    
    
Knapsack_TopDown()
def Recursive(s1,s2,m,n):
    if n==0 or m==0:
        return 0
    pick=0
    non_pick=0
    if s1[m-1]==s2[n-1]:
        pick=Recursive(s1,s2,m-1,n-1)+1
    else:
        non_pick=max(Recursive(s1,s2,m-1,n),Recursive(s1,s2,m,n-1))
    
    return max(pick,non_pick)




def solve():
    s1="abcd"
    s2="abcd"
    m=len(s1)
    n=len(s2)
    res=Recursive(s1,s2,m,n)
    print("Recursive: ",res)

solve()

#Lettcode --> Longest Common Subsequence 1143

#By Top Down Appraoch
def TopDown(s1,s2,m,n,t):
    if n==0 or m==0:
        return 0
    
    
    for i in range(1,m+1):
        for j in range(1,n+1):
            if s1[i-1]==s2[j-1]:
                t[i][j]=1+t[i-1][j-1]
                
            else:
                t[i][j]=max(t[i-1][j],t[i][j-1])
    
    return t[i][j]
    
    
def solve():
    s1="abd"
    s2="abcd"
    m=len(s1)
    n=len(s2)
    t=[[0 for _ in range(n+1)] for _ in range(m+1)]
    res=TopDown(s1,s2,m,n,t)
    print("By Top Down: ",res)
    #Printing Longest Common Subseq. 
    ls=[]
    i=m
    j=n
    #BackTracking of TopDown Approach
    while i>0 and j>0:
        if s1[i-1]==s2[j-1]:
            ls.append(s1[i-1])
            i-=1
            j-=1
        else:
            if t[i-1][j]>t[i][j-1]:
                i-=1
            else:
                j-=1
    
    # --> Pattern 
    print("LCS is: ", ''.join(ls)[::-1])   
            
            


solve()

#Lettcode --> Longest Common Subsequence 1143






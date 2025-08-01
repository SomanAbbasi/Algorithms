def LC_Susbtring(s1,s2,m,n):
    if n==0 or m==0:
        return 0
    res=0
    t=[[0 for _ in range(n+1)] for _ in range(m+1)]
    for i in range(1,m+1):
        for j in range(1,n+1):
            if s1[i-1]==s2[j-1]:
                t[i][j]=1+t[i-1][j-1]
                res=max(res,t[i][j])
            else:
                t[i][j]=0
    
    return res
    
    




def solve():
    s1="abd"
    s2="abcd"
    m=len(s1)
    n=len(s2)
    res=LC_Susbtring(s1,s2,m,n)
    print("res: ",res)


solve()

#Lettcode --> Longest Common Subsequence 1143



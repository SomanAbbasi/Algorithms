
s="aabba"
n=len(s)
t=[[False]*n for _ in range(n)]

#For First Character

for i in range(n):
    t[i][i]=True
#For Two Char
for i in range(n-1):
    t[i][i+1]=s[i]==s[i+1]

for length in range(3,n+1):
    for i in range(n-length+1):
        j=i+length-1
        t[i][j]=(s[i]==s[j]) and t[i+1][j-1]
    
print(t)

"""
import sys

class Solution:
   


    def minCut(self, s: str) -> int:
        i=0
        n=len(s)
        j=n-1
        isPallinrome=[[False]*n for _ in range(n)]
        for i in range(n):
            isPallinrome[i][i]=True
        for i in range(n-1):
            isPallinrome[i][i+1]=s[i]==s[i+1]
        for length in range(3,n+1):
            for i in range(n-length+1):
                j=i+length-1
                isPallinrome[i][j]=(s[i]==s[j]) and isPallinrome[i+1][j-1]
            
        
        t=[0]*n
        for i in range(n):
            if isPallinrome[0][i]:
                t[i]=0
            else:
                min_cuts=float('inf')
                for j in range(i):
                    if isPallinrome[j+1][i]:
                        min_cuts=min(min_cuts,t[j]+1)
                t[i]=min_cuts
        
        return t[n-1]


"""
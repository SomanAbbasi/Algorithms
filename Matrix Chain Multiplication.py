import sys

def MCM(arr,i,j,t):
    
    if i==j:  #When there's only one matrix left no multiplication needed
        return 0
    if t[i][j]!=-1:
        return t[i][j]
    ans=sys.maxsize
    
    for k in range(i,j):
        tempAns=MCM(arr,i,k,t)+MCM(arr,k+1,j,t)+arr[i-1]*arr[k]*arr[j]
        ans=min(ans,tempAns)
    
    t[i][j]=ans
    
    return ans



def main():
    arr=[3,1,5,8]
    n=len(arr)
    t=[[-1 for _ in range(n)] for _ in range(n)]
    res=MCM(arr,1,n-1,t)
    print("MCM: ",res)


main()



"""
Scramble String -> https://www.interviewbit.com/problems/scramble-string/


class Solution:
    def solve(self,a,b):
        n=len(a)
        if a==b:
            return True
        if n<1:
            return False
        
        flag=False
        
        for i in range(1,n):
            #no swap
            no_swap=self.solve(a[:i],b[:i]) and self.solve(a[i:],b[i:])
            swap=self.solve(a[:i],b[n-i:]) and self.solve(a[i:],b[:n-i])
            if swap or no_swap:
                flag=True
                break
        return flag
        
    
    def isScramble(self,A,B):
        l1=len(A)
        l2=len(B)
        if l1!=l2:
            return False
        if not A and not B:
            return True
        res=self.solve(A,B)
        if res:
            return 1
        else:
            return 0
        #print(res)

s1=Solution()
s1.isScramble("phqtrnilf","ilthnqrpf")
        

========= Here is memorize version ========

from functools import lru_cache

class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        if not s1 and not s2:
            return True

        @lru_cache(maxsize=None)
        def solve(a: str, b: str) -> bool:
            if a == b:
                return True
            if sorted(a) != sorted(b):  
                return False
            
            n = len(a)
            for i in range(1, n):
                # No swap case
                if solve(a[:i], b[:i]) and solve(a[i:], b[i:]):
                    return True
                # Swap case
                if solve(a[:i], b[-i:]) and solve(a[i:], b[:-i]):
                    return True
            return False

        res= solve(s1, s2)
        if res:
            return 1
        else:
            return 0

        

"""

    
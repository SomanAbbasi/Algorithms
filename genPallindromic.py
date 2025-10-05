
def gen_pallindromic(n):
    pallindromic=[]
    max_len=len(str(n))
    
    for length in range(1,max_len+1):
        half_ln=(length+1)//2
        start=10**(half_ln-1) if half_ln>1 else 1
        end=10**half_ln
        for half in range(start,end):
            half_str=str(half)
            #Even pal
            even_p=int(half_str+half_str[::-1])
            if even_p<=n:
                pallindromic.append(even_p)
            
            #Odd pal
            odd_p=int(half_str+half_str[-2::-1])
            if odd_p<=n:
                pallindromic.append(odd_p)
    return pallindromic

n=13
ans=gen_pallindromic(n)
print(ans)

    
    





## OPTIMIZE Greedy Approach
# def solve():
#     t=int(input())
#     half=1
#     pallindromic=[]
#     while True:
#         half_str=str(half)
        
#         odd=int(half_str+half_str[-2::-1])
        
#         if odd>t:
#             break
#         pallindromic.append(odd)
        
#         even=int(half_str+half_str[::-1])
#         if even<=t:
#             pallindromic.append(even)
#         half+=1
            
#     print(pallindromic)
        
# solve()



""""
Case 1: SubArray sum(+ve)  Current el (+ve) ---> Extend The Sub Array
Case 2: SubArray sum(-ve)  Current el (+ve) ---> Make New Sub Array
Case 3: SubArray sum(+ve)  Current el (-ve) ---> Extend The Sub Array
Case 4: SubArray sum(-ve)  Current el (-ve) ---> Make New Sub Array

"""
# Time Complexity Order O(n)


def maxSubarray(nums):
    n=len(nums)
    maxEndingHere=maxSoFar=nums[0]
    #res=float('-inf')
    for i in range(1,n):
       maxEndingHere=max(nums[i],maxEndingHere+nums[i])
       maxSoFar=max(maxSoFar,maxEndingHere)
    
    return maxSoFar


nums = [1,-3,2,3,-4]
res=maxSubarray(nums)
print("Max SubArray Sum is ",res)
            


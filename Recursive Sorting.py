
def insertion(arr,k):
    if len(arr)==0 or arr[-1]<=k:
        arr.append(k)
        return
    
    last=arr.pop()
    insertion(arr,k)
    arr.append(last)


def recursive_sort(arr,n):
    if n<=1:
        return arr
    
    last=arr.pop()
    recursive_sort(arr,n-1)
    
    insertion(arr,last)
    
    
arr=[5,4,3,2,0,1]
n=len(arr)

recursive_sort(arr,n)

print(arr)
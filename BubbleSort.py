#Time Complexity Big O(n^2)

def BubbleSort(arr):
    n=len(arr) 
    for i in range(n):
        swapped=False
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapped=True
        if not swapped:
            break
    return arr  
print("Enter list element: ")
arr=list(map(int,input().split()))
result=BubbleSort(arr)
print("Sorted arr: ",result)  





    
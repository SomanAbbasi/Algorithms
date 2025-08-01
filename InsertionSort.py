#Time Complexity
#Best Case O(n)
#Average Case O(n^2)
#Worst Case O(n^2)
def InsertionSort(arr):
    n=len(arr)
    for i in range(1,n):
        key=arr[i]
        j=i-1
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return arr
ls=list(map(int,input().split()))
print(f"Sorted array is: {InsertionSort(ls)} ")





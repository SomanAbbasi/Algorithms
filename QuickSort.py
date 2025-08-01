def Partition(arr,low,high):
    p=arr[low]
    i=low+1
    j=high
    while True:
        while i<=j and arr[i]<=p:
            i+=1
        while i<=j and arr[j]>=p:
            j-=1
        if i<=j:
            arr[i],arr[j]=arr[j],arr[i]
        else:
            break
    arr[low],arr[j]=arr[j],arr[low]
    return j

def QuickSort(arr,low,high):
    if low<high:
        pivot=Partition(arr,low,high)
        QuickSort(arr,low,pivot-1)
        QuickSort(arr,pivot+1,high)
    return arr

arr=list(map(int,input().split()))
print(".....QuickSort.....")
print(QuickSort(arr,0,len(arr)-1))

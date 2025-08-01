# .....Time Complexity.....
#     O(nlogn)


def MergeSort(arr):
    if len(arr)==1:
        return arr
    mid=len(arr)//2
    l_half=arr[:mid]
    r_half=arr[mid:]
    l_half=MergeSort(l_half)
    r_half=MergeSort(r_half)
    return Merge(l_half,r_half)

def Merge(left,right):
    results=[]
    i=0
    j=0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            results.append(left[i])
            i+=1
        else:
            results.append(right[j])
            j+=1
    results.extend(left[i:])
    results.extend(right[j:])
    return results

ls=list(map(int,input().split()))
print("......MergeSort......")
print(MergeSort(ls))    


# Python3 program to find k'th smallest from list
def kthSmallest(arr, k):  
    arr.sort()   
    return arr[k-1] 

print("K'th smallest element is",  kthSmallest([12, 3, 5, 7, 19,23,2], 2)) 
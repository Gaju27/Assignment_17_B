# Program to Split first N natural numbers into two sets with minimum absolute difference of their sums
def 3(N):
     
    # Stores the sum of
    # elements of set1
    sumSet1 = 0
 
    # Stores the sum of
    # elements of set2
    sumSet2 = 0
 
    # Traverse first N
    # natural numbers
    for i in reversed(range(N + 1)):
         
        # Check if sum of elements of
        # set1 is less than or equal
        # to sum of elements of set2
        if sumSet1 <= sumSet2:
           sumSet1 = sumSet1 + i
        else:
           sumSet2 = sumSet2 + i
       
    return abs(sumSet1 - sumSet2)
 
# Driver Code
N = 6
 
print(minAbsDiff(N))
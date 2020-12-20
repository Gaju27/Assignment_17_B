# Count decrements to nearest smaller element required to make all array elements equal
# Input: arr[] = {2, 5, 4, 3, 5, 4}
# Output: 11
# Explanation:
# Step 1: Replace all 5s with 4s. Therefore, arr[] = {2, 4, 4, 3, 4, 4}. Count of operations = 2
# Step 2: Replace all 4s with 3s. Therefore, arr[] = {2, 3, 3, 3, 3, 3}. Count of operations = 4
# Steps 3: Replace all 3s with 2s. Therefore, arr[] = {2, 2, 2, 2, 2, 2}. Count of operations = 5
# Therefore, total number of operations = 11
#
# Input : arr[] = {2, 2, 2}
# Output : 0


# Python3 program for the above approach
import sys


# Function to prthe minimum number of
# decrements to make all elements equals
def MinimumNoOfOperations(arr, n):
    # Find minimum element
    min_ele = sys.maxsize

    for i in range(n):
        min_ele = min(min_ele, arr[i])

    # Stores frequencies of array elements
    mp = {}

    # Update frequencies in the Map
    for i in range(n):
        if (arr[i] == min_ele):
            continue
        else:
            mp[arr[i]] = mp.get(arr[i], 0) + 1

    # Stores the count of
    # decrements at each iteration
    prev_val = 0

    # Stores the total
    # count of derements
    ans = 0

    # Calculate the number of decrements
    for it in mp:
        ans += (mp[it] + prev_val)
        prev_val += mp[it]

    # Return minimum operations
    return ans


# Driver Code
if __name__ == '__main__':
    # Given array
    arr = [2, 5, 4, 3, 5, 4]

    # Given size
    size = len(arr)

    # Function call
    print(MinimumNoOfOperations(arr, size))
# Sum of absolute differences of indices of occurrences of each array element
#
# Given an array arr[] consisting of N integers, the task for each array element arr[i] is to print the sum of |i – j| for all possible indices j such that arr[i] = arr[j].
#

# Python3 program for the above approach
from collections import defaultdict


# Function to find sum of differences
# of indices of occurrences of each
# unique array element
def sum_i(arr, n):
    # Stores indices of each
    # array element
    mp = defaultdict(lambda: [])

    # Store the indices
    for i in range(n):
        mp[arr[i]].append(i)

    # Stores the sums
    ans = [0] * n

    # Traverse the array
    for i in range(n):

        # Find sum for each element
        sum = 0

        # Iterate over the Map
        for it in mp[arr[i]]:
            # Calculate sum of
            # occurrences of arr[i]
            sum += abs(it - i)

            # Store sum for
            # current element
            ans[i] = sum

    # Print answer for each element
    for i in range(n):
        print(ans[i], end=" ")


# Driver code
if __name__ == '__main__':
    # Given array
    arr = [1, 3, 1, 1, 2]

    # Given size
    n = len(arr)

    # Function Call
    sum_i(arr, n)

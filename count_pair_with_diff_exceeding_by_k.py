# Count pairs from two arrays with difference exceeding K | set 2
# Given two integer arrays arr[] and brr[] consistingof distinct elements of size  N and M respectively and an integer K, the task is to find the count of pairs(arr[i], brr[j]) such that(brr[j] – arr[i]) > K.

# Python3 program for the above approach
from bisect import bisect_left, bisect_right


# Function to count pairs that satisfy
# the given conditions
def countPairs(v1, v2, n, m, k):
    # Stores the count of pairs
    count = 0

    # If v1[] is smaller than v2[]
    if (n <= m):

        # Sort the array v1[]
        v1 = sorted(v1)

        # Traverse the array v2[]
        for j in range(m):
            # Returns the address of
            # the first number which
            # is >= v2[j] - k
            index = bisect_left(v1, v2[j] - k)

            # Increase the count by all
            # numbers less than v2[j] - k
            count += index

    # Otherwise
    else:

        # Sort the array v2[]
        v2 = sorted(v2)

        # Traverse the array v1[]
        for i in range(n):
            # Returns the address of
            # the first number which
            # is > v1[i] + k
            index = bisect_right(v2, v1[i] + k)

            # Increase the count by all
            # numbers greater than v1[i] + k
            count += m - index

    # Return the total count of pairs
    return count


# Driver Code
if __name__ == '__main__':
    arr = [5, 9, 1, 8]
    brr = [10, 12, 7, 4, 2, 3]

    K = 3

    N = len(arr)
    M = len(brr)

    print(countPairs(arr, brr, N, M, K))
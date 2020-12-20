# Maximum sum subarray of size K with sum less than X
# Given an array arr[] and two integers K and X, the task is to find the maximum sum among all subarrays of size K with the sum less than X.

# Python3 program for the above approach

# Function to calculate maximum sum
# among all subarrays of size K
# with the sum less than X
def maxSumSubarr(A, N, K, X):
    # Initialize sum_K to 0
    sum_K = 0

    # Calculate sum of first K elements
    for i in range(0, K):
        sum_K += A[i]

    Max_Sum = 0

    # If sum_K is less than X
    if (sum_K < X):
        # Initialize MaxSum with sum_K
        Max_Sum = sum_K

    # Iterate over the array from
    # (K + 1)-th index
    for i in range(K, N):

        # Subtract the first element
        # from the previous K elements
        # and add the next element
        sum_K -= (A[i - K] - A[i])

        # If sum_K is less than X
        if (sum_K < X):
            # Update the Max_Sum
            Max_Sum = max(Max_Sum, sum_K)

    print(Max_Sum)


# Driver Code
arr = [-5, 8, 7, 2, 10,
       1, 20, -4, 6, 9]
K = 5
X = 30

# Size of Array
N = len(arr)

# Function Call
maxSumSubarr(arr, N, K, X)

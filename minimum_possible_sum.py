# Minimum sum possible by assigning every increasing/decreasing consecutive pair with values in that order
#
# Given an array arr[] of size N, the task is to find the minimum sum of positive integers that can be assigned to each array element arr[i],
# such that if arr[i] > arr[i + 1] or arr[i – 1],
# then the positive integer assigned to arr[i] must exceed the integer assigned to arr[i + 1] or arr[i – 1].

# Python3 program for the
# above approach

# Function to print the minimum
# sum of values assigned to each
# element of the array as per
# given conditions
def minSum(arr, n):
    # Initialize vectors with
    # value 1
    ans = [1] * (n)

    # Traverse from left to
    # right
    for i in range(1, n):

        # Update if ans[i] >
        # ans[i-1]
        if (arr[i] > arr[i - 1]):
            ans[i] = max(ans[i],
                         ans[i - 1] + 1)

    # Traverse from right
    # to left
    for i in range(n - 2,
                   -1, -1):

        # Update as ans[i] >
        # ans[i+1] if arr[i] >
        # arr[i+1]
        if (arr[i] > arr[i + 1]):
            ans[i] = max(ans[i],
                         ans[i + 1] + 1)

    # Find the minimum sum
    s = 0
    for x in ans:
        s = s + x

    # Print the sum
    print(s)


# Driver Code
if __name__ == "__main__":
    # Given array arr[]
    arr = [1, 2, 2]

    N = len(arr)

    # Function Call
    minSum(arr, N)
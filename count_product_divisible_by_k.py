# Given an array arr[] of size N and an integer K, the task is to count the number of subsets from the given array with product of elements divisible by K

# Python3 program to
# implement the above
# approach

# Function to count the
# subsets whose product
# of elements is divisible
# by K


def cntSubDivK(arr, N, K,
               rem, dp):
    # If count of elements
    # in the array is 0
    if (N == 0):
        # If rem is 0, then
        # return 1 Otherwise,
        # return 0
        return rem == 0

    # If already computed
    # subproblem occurred
    if (dp[N][rem] != -1):
        return dp[N][rem]

    # Stores count of subsets
    # having product divisible
    # by K when arr[N - 1]
    # present in the subset
    X = cntSubDivK(arr, N - 1, K,
                   (rem * arr[N - 1]) % K, dp)

    # Stores count of subsets having
    # product divisible by K when
    # arr[N - 1] not present in
    # the subset
    Y = cntSubDivK(arr, N - 1,
                   K, rem, dp)

    # Return total subset
    return X + Y


# Utility Function to count
# the subsets whose product of
# elements is divisible by K
def UtilCntSubDivK(arr, N, K):
    # Initialize a 2D array to
    # store values of overlapping
    # subproblems
    dp = [[-1 for x in range(K + 1)]
          for y in range(N + 1)]

    return cntSubDivK(arr, N,
                      K, 1, dp)


# Driver Code
if __name__ == "__main__":
    arr = [1, 2, 3,
           4, 5, 6]
    K = 60
    N = len(arr)
    print(UtilCntSubDivK(arr, N, K))
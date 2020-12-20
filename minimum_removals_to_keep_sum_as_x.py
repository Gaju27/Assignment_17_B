# Minimum removals required such that sum of remaining array modulo M is X
# Input: arr[] = {3, 2, 1, 2}, M = 4, X = 2
# Output: 1
# Explanation: One of the elements at indices (0-based) 1 or 3 can be removed. If arr[1] is removed, then arr[] modifies to {3, 1, 2} and sum % M = 6 % 4 = 2 which is equal to X = 2.
#
# Input: arr[] = {3, 2, 1, 3}, M = 4, X = 3
# Output: 1
# Explanation: Remove element arr[1]( = 2). Therefore, arr[] modifies to {3, 1, 3} and sum % M = 7 % 4 = 3 which is equal to X = 3.

# Python3 program for the above approach
import sys


# Function to find the minimum
# elements having sum x
def findSum(S, n, x):
    # Initialize dp table
    table = [[0 for x in range(x + 1)]
             for y in range(n + 1)]

    for i in range(1, x + 1):
        table[0][i] = sys.maxsize - 1

    # Pre-compute subproblems
    for i in range(1, n + 1):
        for j in range(1, x + 1):

            # If mod is smaller than element
            if (S[i - 1] > j):
                table[i][j] = table[i - 1][j]

            else:

                # Minimum elements with sum
                # j upto index i
                table[i][j] = min(table[i - 1][j],
                                  table[i][j - S[i - 1]] + 1)

    # Return answer
    if (table[n][x] > n):
        return -1

    return table[n][x]


# Function to find minimum number
# of removals to make sum % M in
# remaining array is equal to X
def minRemovals(arr, n, m, x):
    # Sum of all elements
    sum = 0
    for i in range(n):
        sum += arr[i]

    # Sum to be removed
    requied_Sum = 0

    if (sum % m < x):
        requied_Sum = m + sum % m - x
    else:
        requied_Sum = sum % m - x

    # Print answer
    print(findSum(arr, n,
                  requied_Sum))


# Driver Code
if __name__ == "__main__":
    # Given array
    arr = [3, 2, 1, 2]

    # Given size
    n = len(arr)

    # Given mod and x
    m = 4
    x = 2

    # Function call
    minRemovals(arr, n, m, x)
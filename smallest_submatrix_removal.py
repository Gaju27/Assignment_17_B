# Smallest submatrix required to be removed such that sum of the remaining matrix is divisible by K
#
# Input: mat[][] = { {6, 2, 6}, {3, 2, 8}, {2, 5, 3} }, K = 3
# Output: 2
# Explanation:
# Remove the sub-matrix { mat[1][1], mat[2][1] } from the given matrix.
# Since the sum of the remaining matrix is equal to 30 which is divisible by K(=3). Therefore, the required output is 1 * 2 = 2.
#
# Input: mat[][] = { {16, 2, 6, 13}, {33, 21, 8, 8}, {31, 5, 3, 11} }, K = 15
# Output: 3

# Python3 program to implement
# the above approach
import sys


# Function to find the length of the
# smallest subarray to be removed such
# that sum of elements is equal to S % K
def removeSmallestSubarray(arr, S, n, k):
    # Remainder when total_sum
    # is divided by K
    target_remainder = S % k

    # Stores curr_remainder and the
    # most recent index at which
    # curr_remainder has occured
    map1 = {}
    map1[0] = -1

    curr_remainder = 0

    # Stores required answer
    res = sys.maxsize

    for i in range(n):

        # Add current element to
        # curr_sum and take mod
        curr_remainder = (curr_remainder +
                          arr[i] + k) % k

        # Update current
        # remainder index
        map1[curr_remainder] = i

        mod = (curr_remainder -
               target_remainder + k) % k

        # If mod already exists in map
        # the subarray exists
        if (mod in map1):
            # Update res
            res = min(res, i - map1[mod])

    # If not possible
    if (res == sys.maxsize or res == n):
        res = -1

    # Return the result
    return res


# Function to find the smallest submatrix
# rqured to be deleted to make the sum
# of the matrix divisible by K
def smstSubmatDeleted(mat, N, M, K):
    # Stores the sum of
    # element of the matrix
    S = 0

    # Traverse the matrix mat[][]
    for i in range(N):
        for j in range(M):
            # Update S
            S += mat[i][j]

    # Stores smallest area need to be
    # deleted to get sum divisible by K
    min_area = N * M

    # Stores leftmost column
    # of each matrix
    left = 0

    # Stores rightmost column
    # of each matrix
    right = 0

    # Stores number of coulmns
    # deleted of a matrix
    width = 0

    # Store area of the deleted matrix
    area = 0

    # prefixRowSum[i]: Store sum of sub matrix
    # whose topmost left and bottommost right
    # position is (0, left) (i, right)
    prefixRowSm = [0] * N

    # Iterate over all possible values
    # of (left, right)
    for left in range(M):

        # Initialize all possible values
        # of prefixRowSum[] to 0
        prefixRowSum = [0] * N

        for right in range(left, M):

            # Traverse each row from
            # left to right column
            for i in range(N):
                # Update row_sum[i]
                prefixRowSum[i] += mat[i][right]

            # Update width
            width = removeSmallestSubarray(
                prefixRowSum, S, N, K)

            # If no submatrix of the length
            # (right  - left + 1) found to get
            # the required output
            if (width != -1):

                # Update area
                area = (right - left + 1) * (width)

                # If area is less than min_area
                if (area < min_area):
                    # Update min_area
                    min_area = area

    return min_area


# Driver Code
if __name__ == '__main__':
    mat = [[6, 2, 6],
           [3, 2, 8],
           [2, 5, 3]]

    K = 3

    # Stores number of rows
    # in the matrix
    N = len(mat)

    # Stores number of column
    # in the matrix
    M = len(mat[0])

    print(smstSubmatDeleted(mat, N, M, K))
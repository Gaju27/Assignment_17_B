# Check if rows of a Matrix can be rearranged to make Bitwise XOR of first column non-zero
# Input: mat[][] = {{1, 1, 2}, {2, 2, 2}, {3, 3, 3}}
# Output: Yes
# Explanation:
# After rearranging the first row as 2, 1, 1.
# Bitwise XOR of the first column will be 3 i.e., (2 ^ 2 ^ 3).
#
# Input: mat[][] = {{1, 1, 1}, {2, 2, 2}, {3, 3, 3}}
# Output: No
# Explanation:
# As all the rearrangements give same first element so the only combination is (1 ^ 2 ^ 3) which equals zero.
# Therefore, it is not possible to obtain non-zero Bitwise XOR of the first column.

# Python3 program for the above approach

# Function to check if there is any
# row where number of unique elements
# are greater than 1
def checkRearrangements(mat, N, M):
    # Iterate over the matrix
    for i in range(N):
        for j in range(1, M):
            if (mat[i][0] != mat[i][j]):
                return "Yes"

    return "No"


# Function to check if it is possible
# to rearrange mat[][] such that XOR
# of its first column is non-zero
def nonZeroXor(mat, N, M):
    res = 0

    # Find bitwise XOR of the first
    # column of mat[][]
    for i in range(N):
        res = res ^ mat[i][0]

    # If bitwise XOR of the first
    # column of mat[][] is non-zero
    if (res != 0):
        return "Yes"

    # Otherwise check rearrangements
    else:
        return checkRearrangements(mat, N, M)


# Driver Code
if __name__ == "__main__":
    # Given Matrix mat[][]
    mat = [[1, 1, 2],
           [2, 2, 2],
           [3, 3, 3]]

    N = len(mat)
    M = len(mat[0])

    # Function Call
    print(nonZeroXor(mat, N, M))
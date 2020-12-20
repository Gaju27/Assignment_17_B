# Non-negative pairs with sum of Bitwise OR and Bitwise AND equal to N
# Input: N = 5
# Output: (0, 5), (1, 4), (2, 3), (3, 2), (4, 1), (5, 0)
# Explanation: All
# possible
# pairs
# satisfying
# the
# necessary
# conditions:
#
# (0 | 5) + (0 & 5) = 5 + 0 = 5
# (1 | 4) + (1 & 4) = 5 + 0 = 5
# (2 | 3) + (2 & 3) = 3 + 2 = 5
# (3 | 2) + (3 & 2) = 3 + 2 = 5
# (4 | 1) + (4 & 1) = 5 + 0 = 5
# (5 | 0) + (5 & 0) = 5 + 0 = 5
# Input: N = 7
# Output: (0, 7), (1, 6), (2, 5), (3, 4), (4, 3), (5, 2), (6, 1), (7, 0)
# Explanation: All
# possible
# pairs
# satisfying
# the
# necessary
# conditions:
#
# (0 | 7) + (0 & 7) = 7 + 0 = 7
# (1 | 6) + (1 & 6) = 7 + 0 = 7
# (2 | 5) + (2 & 5) = 7 + 0 = 7
# (3 | 4) + (3 & 4) = 7 + 0 = 7
# (4 | 3) + (4 & 3) = 7 + 0 = 7
# (5 | 2) + (5 & 2) = 7 + 0 = 7
# (6 | 1) + (6 & 1) = 7 + 0 = 7
# (7 | 0) + (7 & 0) = 7 + 0 = 7


# Python3 program for the above approach

# Function to print all pairs whose
# sum of Bitwise OR and AND is N
def findPairs(N):
    # Iterate from i = 0 to N
    for i in range(0, N + 1):
        # Print pairs (i, N - i)
        print("(", i, ",",
              N - i, "), ", end="")


# Driver code
if __name__ == "__main__":
    N = 5

    findPairs(N)
# Sum of all possible triplet products from given ranges
# Input: A = 1, B = 1, C = 2
# Output: 3
# Explanation: The value of the given expression is: (1 * 1 * 1 + 1 * 1 * 2) % (109 + 7) = 3
# Therefore, the required output is 3.
#
# Python3 program to implement
# the above approach
M = 1000000007


# Function to find the sum
# of all possible triplet
# products (i * j * k)
def findTripleSum(A, B, C):
    # Stores sum required sum
    sum = 0

    # Iterate over all
    # possible values of i
    for i in range(1, A + 1):

        # Iterate over all
        # possible values of j
        for j in range(1, B + 1):

            # Iterate over all
            # possible values of k
            for k in range(1, C + 1):
                # Stores the product
                # of (i * j *k)
                prod = (((i % M) * (j % M)) %
                        M * (k % M)) % M

                # Update sum
                sum = (sum + prod) % M

    return sum


# Driver Code
if __name__ == '__main__':
    A = 10
    B = 100
    C = 1000

    print(findTripleSum(A, B, C))
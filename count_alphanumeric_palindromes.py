# Count alphanumeric palindromes of length N
# Input: N = 2
# Output: 62
# Explanation: There are 26 palindromes of the form {“AA”, “BB”, …, “ZZ”}, 26 palindromes of the form {“aa”, “bb”, …, “cc”} and 10 palindromes of the form {“00”, “11”, …, “99”}. Therefore, the total number of palindromic strings = 26 + 26 + 10 = 62.
#
# Input: N = 3
# Output: 3844


# Python3 program for the above approach

# Function to calculate (x ^ y) mod p
def power(x, y, p):
    # Initialize result
    res = 1

    # Update x if it is more
    # than or equal to p
    x = x % p

    if (x == 0):
        return 0

    while (y > 0):

        # If y is odd, multiply
        # x with result
        if ((y & 1) == 1):
            res = (res * x) % p

        # y must be even now
        y = y >> 1
        x = (x * x) % p

    # Return the final result
    return res


# Driver Code

# Given N
N = 3

# Base Case
if ((N == 1) or (N == 2)):
    print(62)

else:

    m = (10 ** 9) + 7

    # Check whether n
    # is even or odd
    if (N % 2 == 0):
        k = N // 2
        flag = True
    else:
        k = (N - 1) // 2
        flag = False

    if (flag):

        # Function Call
        a = power(62, k, m)
        print(a)
    else:

        # Function Call
        a = power(62, (k + 1), m)
        print(a)
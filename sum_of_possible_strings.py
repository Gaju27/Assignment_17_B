# Sum of all possible strings obtained by removal of non-empty substrings
# Input: str = “205”
# Output: 57
# Explanation: Substrings that can be removed are “2”, “0”, “5”, “20”, “05”, “205”. The resultant strings are “05”, “25”, “20”, “5”, “2”, “0” respectively. Therefore, the sum will be 57.
#
# Input: str = “1234”
# Output: 680
# Explanation: Substrings that can be removed are “1”, “2”, “3”, “4”, “12”, “23”, “34”, “123”, “234”, “1234”. The resultant strings are “234”, “134”, “124”, “123”, “34”, “14”, “12”, “4”, “1”, “0” respectively. Therefore, the sum will be 680.


# Python 3 program for the
# above approach
N = 10
pref = [0] * N
power = [0] * N


# Function to convert a
# character to its equivalent
# digit
def toDigit(ch):
    return (ord(ch) -
            ord('0'))


# Function to precompute
# powers of 10
def powerOf10():
    power[0] = 1
    for i in range(1, N):
        power[i] = power[i - 1] * 10


# Function to precompute prefix sum
# of numerical strings
def precomputePrefix(st, n):
    pref[0] = (ord(st[0]) -
               ord('0'))
    for i in range(1, n):
        pref[i] = (pref[i - 1] +
                   toDigit(st[i]))


# Function to return the i-th
# term of Triangular Number
def triangularNumber(i):
    res = i * (i + 1) // 2
    return res


# Function to return the sum
# of all resulting strings
def sumOfSubstrings(st):
    n = len(st)

    # Precompute powers
    # of 10
    powerOf10()

    # Precompute prefix
    # sum
    precomputePrefix(st, n)

    # Initialize result
    ans = 0

    for i in range(n - 1):
        # Apply the above general
        # formula for every i
        ans += ((pref[n - i - 2] * (i + 1) +
                 toDigit(st[n - i - 1]) *
                 triangularNumber(n - i - 1)) *
                power[i])

    # Return the answer
    return ans


# Driver Code
if __name__ == "__main__":
    st = "1234"

    # Function Call
    print(sumOfSubstrings(st))
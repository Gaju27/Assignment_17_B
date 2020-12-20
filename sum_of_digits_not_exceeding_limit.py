# Smallest number greater than or equal to N having sum of digits not exceeding S
# Given integer N and integer S, the task is to find the smallest number greater than or equal to N such that the sum of its digits does not exceed S.
#
# Input: N = 3, S = 2
# Output: 10
# Explanation: Sum of digits of 10 is 1, which is less than 2.
#
# Input: N = 19, S = 3
# Output: 20
# Explanation: Sum of digits of 20 is 2, which is less than 3.


# Python program for the above approach

# Function to calculate
# sum of digits of n
def sum(n):
    sm = 0
    while (n > 0):
        sm += n % 10
        n //= 10
    return sm


# Function to find the smallest
# possible integer satisfying the
# given condition
def smallestNumber(n, s):
    # If sum of digits is
    # already smaller than s
    if (sum(n) <= s):
        return n

    # Initialize variables
    ans, k = n, 1

    for i in range(9):

        # Find the k-th digit
        digit = (ans // k) % 10

        # Add remaining
        add = k * ((10 - digit) % 10)

        ans += add

        # If sum of digits
        # does not exceed s
        if (sum(ans) <= s):
            break

        # Update K
        k *= 10

    # Return answer
    return ans


# Driver Code

# Given N and S
n, s = 3, 2

# Function call
print(smallestNumber(n, s))
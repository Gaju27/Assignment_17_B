# Probability of obtaining Prime Numbers as product of values obtained by throwing N dices
# Given an integer N denoting the number of dices, the task is to find the probability of the product of numbers appearing on the top faces of N thrown dices being a prime number. All N dices must be thrown simultaneously.
#
# Input: N = 2
# Output: 6 / 36
# Explanation:
# On throwing N(=2) dices simultaneously, the possible outcomes on the top faces of N(=2) dices having product equal to a prime number are: {(1, 2), (1, 3), (1, 5), (2, 1), (3, 1), (5, 1)}.
# Therefore, the count of favourable outcomes = 6 and the count of the sample space is = 36
# Therefore, the required output is (6 / 36)
#
# Input: N = 3
# Output: 9 / 216

# Python3 program to implement
# the above approach

# Function to find the value
# of power(X, N)
def power(x, N):
    # Stores the value
    # of (X ^ N)
    res = 1

    # Calculate the value of
    # power(x, N)
    while (N > 0):

        # If N is odd
        if (N % 2 == 1):
            # Update res
            res = (res * x)

        # Update x
        x = (x * x)

        # Update N
        N = N >> 1

    return res


# Function to find the probability of
# obtaining a prime number as the
# product of N thrown dices
def probablityPrimeprod(N):
    # Stores count of favorable outcomes
    N_E = 3 * N

    # Stores count of sample space
    N_S = power(6, N)

    # Prthe required probablity
    print(N_E, " / ", N_S)


# Driver code
if __name__ == '__main__':
    N = 2

    probablityPrimeprod(N)
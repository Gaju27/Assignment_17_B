# Count prime pairs whose difference is also a Prime Number
# Input: N = 5
# Output: 2
# Explanations:
# Pair of prime numbers in the range [1, 5] whose difference between elements is also a prime number are:
# (2, 5) = 3 (Prime number)
# (3, 5) = 2 (Prime number)
# Therefore, the count of pairs of the prime numbers whose difference is also a prime number is 2.
#
# Input: N = 11
# Output: 4

# Python3 program to implement
# the above approach
from math import sqrt


# Function to find all prime
# numbers in the range [1, N]
def SieveOfEratosthenes(N):
    # isPrime[i]: Stores if i is
    # a prime number or not
    isPrime = [True for i in range(N + 1)]

    isPrime[0] = False
    isPrime[1] = False

    # Calculate all prime numbers up to
    # Max using Sieve of Eratosthenes
    for p in range(2, int(sqrt(N)) + 1, 1):

        # If P is a prime number
        if (isPrime[p]):

            # Set all multiple of P
            # as non-prime
            for i in range(p * p, N + 1, p):
                # Update isPrime
                isPrime[i] = False

    return isPrime


# Function to count pairs of
# prime numbers in the range [1, N]
# whose difference is prime
def cntPairsdiffOfPrimeisPrime(N):
    # Function to count pairs of
    # prime numbers whose difference
    # is also a prime number
    cntPairs = 0

    # isPrime[i]: Stores if i is
    # a prime number or not
    isPrime = SieveOfEratosthenes(N)

    # Iterate over the range [2, N]
    for i in range(2, N + 1, 1):

        # If i and i - 2 is
        # a prime number
        if (isPrime[i] and isPrime[i - 2]):
            # Update cntPairs
            cntPairs += 2

    return cntPairs


# Driver Code
if __name__ == '__main__':
    N = 5

    print(cntPairsdiffOfPrimeisPrime(N))

# Count pairs from a given range whose sum is a Prime Number in that range
# Input: L = 1, R = 5
# Output: 4
# Explanation: Pairs whose sum is a prime number and in the range [L, R] are { (1, 1), (1, 2), (1, 4), (2, 3) }. Therefore, the required output is 4.
#
# Input: L = 1, R = 100
# Output: 518
#
# # Python program to implement
# # the above approach
import math


# Function to find all prime numbers in range
# [1, lmt] using sieve of Eratosthenes
def simpleSieve(lmt, prime):
    # segmentedSieve[i]: Stores if i is
    # a prime number (True) or not (False)
    Sieve = [True] * (lmt + 1)

    # Set 0 and 1 as non-prime
    Sieve[0] = Sieve[1] = False

    # Iterate over the range [2, lmt]
    for i in range(2, lmt + 1):

        # If i is a prime number
        if (Sieve[i] == True):

            # Append i into prime
            prime.append(i)

            # Set all multiple of i non-prime
            for j in range(i * i,
                           int(math.sqrt(lmt)) + 1, i):
                # Update Sieve[j]
                Sieve[j] = false

    return prime


# Function to find all the prime numbers
# in the range [low, high]
def SegmentedSieveFn(low, high):
    # Stores square root of high + 1
    lmt = int(math.sqrt(high)) + 1

    # Stores all the prime numbers
    # in the range [1, lmt]
    prime = []

    # Find all the prime numbers in
    # the range [1, lmt]
    prime = simpleSieve(lmt, prime)

    # Stores count of elements in
    # the range [low, high]
    n = high - low + 1

    # segmentedSieve[i]: Check if (i - low)
    # is a prime number or not
    segmentedSieve = [True] * (n + 1)

    # Traverse the array prime[]
    for i in range(0, len(prime)):

        # Store smallest multiple of prime[i]
        # in the range[low, high]
        lowLim = int(low // prime[i]) * prime[i]

        # If lowLim is less than low
        if (lowLim < low):

            # Update lowLim
            lowLim += prime[i]

            # Iterate over all multiples of prime[i]
            for j in range(lowLim, high + 1, prime[i]):

                # If j not equal to prime[i]
                if (j != prime[i]):
                    # Update segmentedSieve[j - low]
                    segmentedSieve[j - low] = False

    return segmentedSieve


# Function to count the number of pairs
# in the range [L, R] whose sum is a
# prime number in the range [L, R]
def countPairsWhoseSumPrimeL_R(L, R):
    # segmentedSieve[i]: Check if (i - L)
    #  is a prime number or not
    segmentedSieve = SegmentedSieveFn(L, R)

    # Stores count of pairs whose sum of
    # elements is a prime and in range [L, R]
    cntPairs = 0

    # Iterate over [L, R]
    for i in range(L, R + 1):

        # If (i - L) is a prime
        if (segmentedSieve[i - L] == True):
            # Update cntPairs
            cntPairs += i / 2

    return cntPairs


# Driver Code
if __name__ == '__main__':
    L = 1
    R = 5

    print(countPairsWhoseSumPrimeL_R(L, R))
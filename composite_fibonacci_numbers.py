# Count composite fibonacci numbers from given array
# Given an array arr[] of size N, the task is to find the composite Fibonacci numbers present in the given array.

# Python3 program to implement
# the above approach
import math


# Function to find all Fibonacci
# numbers up to Max
def createhashmap(Max):
    # Store all Fibonacci numbers
    # upto Max
    hashmap = {""}

    # Stores previous element
    # of Fibonacci sequence
    curr = 1

    # Stores previous element
    # of Fibonacci sequence
    prev = 0

    # Insert prev into hashmap
    hashmap.add(prev)

    # Insert all the Fibonacci
    # numbers up to Max
    while (curr <= Max):
        # Insert curr into hashmap
        hashmap.add(curr)

        # Stores curr into temp
        temp = curr

        # Update curr
        curr = curr + prev

        # Update prev
        prev = temp

    return hashmap


# Function to find all Composite
# numbers up to Max
def SieveOfEratosthenes(Max):
    # isPrime[i]: Stores if i is
    # a prime number or not
    isPrime = [1 for x in range(Max + 1)]
    isPrime[0] = 0
    isPrime[1] = 0

    # Calculate all prime numbers up to
    # Max using Sieve of Eratosthenes
    for p in range(0, int(math.sqrt(Max))):

        # If P is a prime number
        if (isPrime[p]):

            # Set all multiple of P
            # as non-prime
            for i in range(2 * p, Max, p):
                isPrime[i] = 0

    return isPrime


# Function to find the numbers which is
# both a composite and Fibonacci number
def cntFibonacciPrime(arr, N):
    # Stores the largest element
    # of the array
    Max = arr[0]

    # Traverse the array arr[]
    for i in range(0, N):
        # Update Max
        Max = max(Max, arr[i])

    # isPrim[i] check i is
    # a prime number or not
    isPrime = SieveOfEratosthenes(Max)

    # Stores all the Fibonacci numbers
    hashmap = createhashmap(Max)

    # Traverse the array arr[]
    for i in range(0, N):

        # Current element is not
        # a composite number
        if arr[i] == 1:
            continue

        # If current element is a Fibonacci
        # and composite number
        if ((arr[i] in hashmap) and
                (not (isPrime[arr[i]]))):
            # Print current element
            print(arr[i], end=" ")


# Driver Code
arr = [13, 55, 7, 3, 5,
       21, 233, 144, 89]
N = len(arr)

cntFibonacciPrime(arr, N)
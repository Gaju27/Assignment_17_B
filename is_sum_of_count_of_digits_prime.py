Given an array A[] consisting of N integers, the task is to check if the sum of numbers of digits in each array element is a prime number or not.

# Python3 program for the above approach
import math


# Function to check whether
# a number is prime or not
def isPrime(n):
    # Corner cases
    if (n <= 1):
        return False
    if (n <= 3):
        return True

    # If given number is a
    # multiple of 2 or 3
    if (n % 2 == 0 or n % 3 == 0):
        return False

    for i in range(5, int(math.sqrt(n) + 1), 6):
        if (n % i == 0 or n % (i + 2) == 0):
            return False

    return True


# Function to check if sum
# of count of digits of all
# array elements is prime or not
def CheckSumPrime(A, N):
    # Initialize sum with 0
    sum = 0

    # Traverse over the array
    for i in range(0, N):
        # Convert array element to string
        s = str(A[i])

        # Add the count of
        # digits to sum
        sum += len(s)

    # Print the result
    if (isPrime(sum) == True):
        print("Yes")
    else:
        print("No")


# Drive Code
if __name__ == '__main__':
    A = [1, 11, 12]

    N = len(A)

    # Function call
    CheckSumPrime(A, N)
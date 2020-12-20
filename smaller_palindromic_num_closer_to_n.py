# Smaller palindromic number closest to N
# Given an integer N, the task is to find the closest palindromic number which is smaller than N.
#
# Input: N = 4000
# Output: 393
# Explanation:
# 3993 is the closest palindromic number to N( = 4000) which is also smaller than N( = 4000). Therefore, 3993 is the required answer.
#
# Input: N = 2889
# Output: 2882


# Python3 program to implement
# the above approach

# Function to check if
# a number is palindrome or not
def checkPalindrome(N):
    # Stores reverse of N
    rev = 0

    # Stores the value of N
    temp = N

    # Calculate reverse of N
    while (N != 0):
        # Update rev
        rev = rev * 10 + N % 10

        # Update N
        N = N // 10

    # Update N
    N = temp

    # If N is equal to
    # rev of N
    if (N == rev):
        return True

    return False


# Function to find the closest
# smaller palindromic number to N
def closestSmallerPalindrome(N):
    # Calculate closest smaller
    # palindromic number to N
    while N >= 0 and not checkPalindrome(N):
        # Update N
        N -= 1

    return N


# Driver Code
if __name__ == '__main__':
    N = 4000

    print(closestSmallerPalindrome(N))
# Check if a right-angled triangle can be formed by the given side lengths
# Input: A = 3, B = 4
# Output: Yes
# Explanation: A right-angled triangle is possible with side lengths 3, 4 and 5.
#
# Input : A = 2, B = 5
# Output: No

# Python3 program to implement
# the above approach
from math import sqrt, floor, ceil


# Function to check if N is a
# perfect square number or not
def checkPerfectSquare(N):
    # If N is a non
    # positive integer
    if (N <= 0):
        return 0

    # Stores square root
    # of N
    sq = sqrt(N)

    # Check for perfect square
    if (floor(sq) == ceil(sq)):
        return 1

    # If N is not a
    # perfect square number
    return 0


# Function to check if given two sides of a
# triangle forms a right-angled triangle
def checktwoSidesareRighTriangle(A, B):
    checkTriangle = False

    # If the value of (A * A + B * B) is a
    # perfect square number
    if (checkPerfectSquare(A * A + B * B)):
        # Update checkTriangle
        checkTriangle = True

    # If the value of (A * A - B * B) is a
    # perfect square number
    if (checkPerfectSquare(A * A - B * B)):
        # Update checkTriangle
        checkTriangle = True

    # If the value of (B * B - A * A) is a
    # perfect square number
    if (checkPerfectSquare(B * B - A * A)):
        # Update checkTriangle
        checkTriangle = True

    return checkTriangle


# Driver Code
if __name__ == '__main__':

    A = 3
    B = 4

    # If the given two sides of a triangle
    # forms a right-angled triangle
    if (checktwoSidesareRighTriangle(A, B)):
        print("Yes")

    # Otherwise
    else:
        print("No")
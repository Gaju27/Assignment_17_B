# Check if it is possible to reach (X, Y) from (1, 1) by given steps
# Input: X = 4, Y = 7
# Output: Yes
# Explanation: Point (4, 7) can be reached by the following steps: (1, 1) -> (1, 2) -> (1, 4) -> (1, 8) -> (1, 7) -> (2, 7) -> (4, 7)
#
# Input: X = 3, Y = 6
# Output: No
#

# Python3 program for the
# above approach

# Function to find the gcd
# of two numbers
def gcd(a, b):
    # Base case
    if (a < b):
        t = a
        a = b
        b = t

    if (a % b == 0):
        return b

    # Recurse
    return gcd(b, a % b)


# Function to print the
# answer
def printAnswer(x, y):
    # GCD of X and Y
    val = gcd(x, y)

    # If GCD is power of 2
    if ((val &
         (val - 1)) == 0):
        print("Yes")
    else:
        print("No")


# Driver code
if __name__ == "__main__":
    # Given X and Y
    x = 4
    y = 7

    # Function call
    printAnswer(x, y)

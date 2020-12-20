# Find a pair with sum N having minimum absolute difference
#
# Given an integerN, the task is to  find a distinct pair of X and Y such that X + Y = N and abs(X – Y) is minimum.
#

# Python3 program to implement
# the above approach

# Function to find the value of X and Y
# having minimum value of abs(X - Y)


def findXandYwithminABSX_Y(N):
    # If N is an odd number
    if (N % 2 == 1):
        print((N // 2), (N // 2 + 1))

    # If N is an even number
    else:
        print((N // 2 - 1), (N // 2 + 1))


# Driver Code
if __name__ == '__main__':
    N = 12

    findXandYwithminABSX_Y(N)
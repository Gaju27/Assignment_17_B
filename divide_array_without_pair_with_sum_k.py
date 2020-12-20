# Divide array into two arrays which does not contain any pair with sum K
#
# Given an array arr[] consisting of N non - negative distinct integers and aninteger K, the task is to distribute the array in two arrays such that both the arrays does not contain a pair with sum K.
#
#
# # Python3 program for the above approach

# Function to split the given
# array into two separate arrays
# satisfying given condition


def splitArray(a, n, k):
    # Stores resultant arrays
    first = []
    second = []

    # Traverse the array
    for i in range(n):

        # If a[i] is smaller than
        # or equal to k/2
        if (a[i] <= k // 2):
            first.append(a[i])
        else:
            second.append(a[i])

    # Print first array
    for i in range(len(first)):
        print(first[i], end=" ")

    # Print second array
    print("\n", end="")
    for i in range(len(second)):
        print(second[i], end=" ")


# Driver Code
if __name__ == '__main__':
    # Given K
    k = 5

    # Given array
    a = [0, 1, 3, 2, 4, 5,
         6, 7, 8, 9, 10]

    n = len(a)

    splitArray(a, n, k)

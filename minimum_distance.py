# Minimum distance to visit given K points on X-axis after starting from the origin
# Python3 program to implement
# the above approach
import sys


# Function to find the minimum distance
# travelled to visit K point
def MinDistK(arr, N, K):
    # Stores minimum distance travelled
    # to visit K point
    res = sys.maxsize

    # Stores distance travelled
    # to visit points
    dist = 0

    # Traverse the array arr[]
    for i in range(N - K + 1):

        # If arr[i] and arr[i + K - 1]
        # are positive
        if (arr[i] >= 0 and arr[i + K - 1] >= 0):

            # Update dist
            dist = max(arr[i], arr[i + K - 1])
        else:

            # Update dist
            dist = (abs(arr[i]) + abs(arr[i + K - 1]) +
                    min(abs(arr[i]), abs(arr[i + K - 1])))

        # Update res
        res = min(res, dist)

    return res


# Driver Code
if __name__ == '__main__':
    K = 3

    # Initial the array
    arr = [-30, -10, 10, 20, 50]

    N = len(arr)

    print(MinDistK(arr, N, K))

# This code is contributed by ipg2016107
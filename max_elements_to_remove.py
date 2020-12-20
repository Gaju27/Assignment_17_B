# Maximum array elements that can be removed along with its adjacent values to empty given array

# Given an array arr[] of size N. In each operation, pick an array element X and remove all array elements in the range [X – 1, X + 1].
# The task is to find the maximum number of steps required such that no coins left in the array.
#
#
# # Python3 program to implement
# the above approach

# Function to find maximum steps to
# remove all coins from the arr[]


def maximumSteps(arr, N):
    # Store the frequency of array
    # elements in ascending order
    Map = {}

    # Traverse the arr[] array
    for i in range(N):
        Map[arr[i]] = Map.get(arr[i], 0) + 1

    # Stores count of steps required
    # to remove all the array elements
    cntSteps = 0

    # Traverse the map
    for i in Map:

        # Stores the smallest element
        # of Map
        X = i

        # If frequency if X
        # greater than 0
        if (Map[i] > 0):

            # Update cntSteps
            cntSteps += 1

            # Mark X as
            # removed element
            Map[X] = 0

            # If frequency of (X + 1)
            # greater than  0
            if (X + 1 in Map):
                # Mark (X + 1) as
                # removed element
                Map[X + 1] = 0

    return cntSteps


# Driver Code
if __name__ == '__main__':
    arr = [5, 1, 3, 2, 6, 7, 4]
    N = len(arr)

    print(maximumSteps(arr, N))
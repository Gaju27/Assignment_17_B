# Rearrange array to maximize count of local minima
#
# Given an array arr[] of size N, the task is to rearrange the array elements such that the count of local minima in the array is maximum.
#
# Note: An element arr[x] is said to be a local minimum if it is less than or equal to both its adjacent elements. The first and last array elements can’t be considered as local minima.


# Python3 program to implement
# the above approach

# Function to rearrange array
# elements to maximize count of
# local minima in the array
def rearrangeArrMaxcntMinima(arr, N):
    # Sort the array in
    # ascending order
    arr.sort()

    # Stores index of
    # left pointer
    left = 0

    # Stores index of
    # right pointer
    right = N // 2

    # Traverse the array elements
    while (left < N // 2 or
           right < N):

        # if right is less
        # than N
        if (right < N):
            # Print array element
            print(arr[right],
                  end=" ")

            # Update right
            right += 1

        if (left < N // 2):
            # Print array element
            print(arr[left],
                  end=" ")

            # Update left
            left += 1


# Driver Code
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    N = len(arr)
    rearrangeArrMaxcntMinima(arr, N)
# Construct array with sum of product of same indexed elements in the given array equal to zero
#
# Input: arr[] = {1, 2, 3, 4}
# Output: -4 -3 2 1
# Explanation:
# Sum of product of same indexed array elements of arr[] with the new array = {1 * (-4) + 2 * (-3) + 3 * (2) + 4 * (1)} = 0.
# Therefore, the required output is -4 -3 2 1.
#
# Input: arr[] = {-1, 2, -3, 6, 4}
# Output: 1 1 1 1 -1

# Python3 program to implement
# the above approach

# Function to generate a new array
# with product of same indexed elements
# with arr[] equal to 0
def constructNewArraySumZero(arr, N):
    # Stores sum of same indexed array
    # elements of arr and new array
    newArr = [0] * N

    # Traverse the array
    for i in range(N):

        # If i is an even number
        if (i % 2 == 0):

            # Insert arr[i + 1] into
            # the new array newArr[]
            newArr[i] = arr[i + 1]

        else:

            # Insert -arr[i - 1] into
            # the new array newArr[]
            newArr[i] = -arr[i - 1]

    # Print new array elements
    for i in range(N):
        print(newArr[i],
              end=" ")


# Driver code
arr = [1, 2, 3, -5, -6, 8]
N = len(arr)
constructNewArraySumZero(arr, N)
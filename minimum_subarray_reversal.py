# Minimum subarray reversals required such that sum of all pairs of adjacent elements is odd

# Input: arr[] = {13, 2, 6, 8, 3, 5, 7, 10, 14, 15}
# Output: 3
# Explanation:
# Step 1: Reverse subarray [2, 4] to modify the array to {13, 2, 3, 8, 6, 5, 7, 10, 14, 15}
# Step 2: Reverse subarray [4, 5] to modify the array to {13, 2, 3, 8, 5, 6, 7, 10, 14, 15}
# Step 3: Reverse subarray [8, 9] to modify the array to {13, 2, 3, 8, 5, 6, 7, 10, 15, 14}
# After the above reversals, the sum of all adjacent element pairs is odd.
# Therefore, the minimum reversals required is 3.
#
# Input: arr[] = {1, 3, 4, 5, 9, 6, 8}
# Output: 2

# Python3 program for the
# above approach

# Function to count reversals
# to seperate elements with
# same parity
def separate(arr, n, parity):
    count = 1
    res = 0

    # Traverse the given array
    for i in range(1, n):

        # Count size of subarray
        # having integers with
        # same parity only
        if (((arr[i] + parity) & 1) and
                ((arr[i - 1] + parity) & 1)):
            count += 1

        # Otherwise
        else:

            # Reversals required is
            # equal to one less than
            # subarray size
            if (count > 1):
                res += count - 1

            count = 1

    # Return the total
    # reversals
    return res


# Function to print the
# array elements
def printArray(arr, n):
    for i in range(n):
        print(arr[i],
              end=" ")


# Function to count the mimimum
# reversals required to make
# make sum of all adjacent
# elements odd
def requiredOps(arr, N):
    # Stores operations required
    # for separating adjacent
    # odd elements
    res1 = separate(arr, N, 0)

    # Stores operations required
    # for separating adjacent
    # even elements
    res2 = separate(arr, N, 1)

    # Maximum of two is the
    # return
    print(max(res1, res2))


# Driver Code
if __name__ == "__main__":
    # Given array arr[]
    arr = [13, 2, 6, 8, 3, 5,
           7, 10, 14, 15]

    # Size of array
    N = len(arr)

    # Function Call
    requiredOps(arr, N)
# Count pairs from two arrays with difference exceeding K
# Given two integer arrays arr[] and brr[] consisting of distinct elements of size N and M respectively and an nteger K, the task is to find the count of pairs(arr[i], brr[j]) such that(brr[j] – arr[i]) > K.
#
# Python3 program to implement
# the above approach

# Function to count pairs that satisfy
# the given conditions
def count_pairs(arr, brr, N, M, K):
    # Stores index of
    # the left pointer.
    i = 0

    # Stores index of
    # the right pointer
    j = 0

    # Stores count of total pairs
    # that satisfy the conditions
    cntPairs = 0

    # Sort arr[] array
    arr = sorted(arr)

    # Sort brr[] array
    brr = sorted(brr)

    # Traverse both the array
    # and count then pairs
    while (i < N and j < M):

        # If the value of
        # (brr[j] - arr[i]) exceeds K
        if (brr[j] - arr[i] > K):

            # Update cntPairs
            cntPairs += (M - j)

            # Update
            i += 1
        else:

            # Update j
            j += 1

    return cntPairs


# Driver Code
if __name__ == '__main__':
    arr = [5, 9, 1, 8]
    brr = [10, 12, 7, 4, 2, 3]
    K = 3

    N = len(arr)
    M = len(brr)

    print(count_pairs(arr, brr, N, M, K))

# Median of all non-empty subset sums
# Input: arr = {2, 3, 3}
# Output: 5
# Explanation:
# Non-Empty Subsets of the given array are: { {2}, {3}, {3}, {2, 3}, {2, 3}, {3, 3}, {2, 3, 3} }.
# Possible sum of each subset are:
# { {2}, {3}, {3}, {5}, {5}, {6}, {8} }
# Therefore, the median of all possible sum of each subset is 5.
#
# Input: arr = {1, 2, 1}
# Output: 2


# Python3 program to implement
# the above approach

# Function to calculate the
# median of all possible subsets
# by given operations
def findMedianOfsubSum(arr, N):
    # Stores sum of elements
    # of arr[]
    sum = 0

    # Traverse the array arr[]
    for i in range(N):
        # Update sum
        sum += arr[i]

        # Sort the array
    arr.sort(reverse=False)

    # DP[i][j]: Stores total number
    # of ways to form the sum j by
    # either selecting ith element
    # or not selecting ith item.
    dp = [[0 for i in range(sum + 1)]
          for j in range(N)]

    # Base case
    for i in range(N):
        # Fill dp[i][0]
        dp[i][0] = 1

        # Base case
    dp[0][arr[0]] = 1

    # Fill all the DP states based
    # on the mentioned DP relation
    for i in range(1, N, 1):
        for j in range(1, sum + 1, 1):

            # If j is greater than
            # or equal to arr[i]
            if (j >= arr[i]):

                # Update dp[i][j]
                dp[i][j] = (dp[i - 1][j] +
                            dp[i - 1][j - arr[i]])
            else:

                # Update dp[i][j]
                dp[i][j] = dp[i - 1][j]

    # Stores all possible
    # subset sum
    sumSub = []

    # Traverse all possible
    # subset sum
    for j in range(1, sum + 1, 1):

        # Stores count of subsets
        # whose sum is j
        M = dp[N - 1][j]

        # Itearate over the
        # range [1, M]
        for i in range(1, M + 1, 1):
            # Insert j into sumSub
            sumSub.append(j)

            # Stores middle element
    # of sumSub
    mid = sumSub[len(sumSub) // 2]

    return mid


# Driver Code
if __name__ == '__main__':
    arr = [2, 3, 3]
    N = len(arr)
    print(findMedianOfsubSum(arr, N))
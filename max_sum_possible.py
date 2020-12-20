# Maximum sum possible from given Matrix by performing given operations
# Given a matrix arr[][] of dimensions 2 * N, the task is to maximize the sum possible by selecting at most one element
# from each column such that no two consecutive elements are chosen from the same row.


# Function to prthe maximum sum
def maxSum(arr, n, m):
    # Dp table
    dp = [[0 for i in range(m + 1)]
          for i in range(2)]

    # Intializing dp array with 0s
    # for (i = 0 i < 2 i++) {
    #     dp[i] = vector<int>(m)
    #     for (j = 0 j < m j++) {
    #         dp[i][j] = 0
    #     }
    # }

    # Base case
    dp[0][m - 1] = arr[0][m - 1]
    dp[1][m - 1] = arr[1][m - 1]

    # Traverse each column
    for j in range(m - 2, -1, -1):

        # Update answer for both rows
        for i in range(2):
            if (i == 1):
                dp[i][j] = max(arr[i][j] + dp[0][j + 1],
                               arr[i][j] + dp[0][j + 2])
            else:
                dp[i][j] = max(arr[i][j] + dp[1][j + 1],
                               arr[i][j] + dp[1][j + 2])

    # Print the maximum sum
    print(max(dp[0][0], dp[1][0]))


# Driver Code
if __name__ == '__main__':
    # Given array
    arr = [[1, 50, 21, 5],
           [2, 10, 10, 5]]

    # Number of Columns
    N = len(arr[0])

    # Function calls
    maxSum(arr, 2, N)
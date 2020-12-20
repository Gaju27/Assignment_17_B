# Count unique paths with given sum in an N-ary Tree
# Given an integer X and integer N, the task is to find the number of unique paths starting from the root in N - ary tree
# such that the sum of all these paths is equal to X.The N - ary tree satisfies the following conditions:
# All the nodes have N children and the weight of each edge is distinct and lies in the range[1, N].
# The tree is extended up to the infinity.

# Python3 program for the above approach
mod = int(1e9 + 7)


# Function for counting total
# no of paths possible with
# the sum is equal to X
def findTotalPath(X, n, dp):
    # If the path of the sum
    # from the root to current
    # node is stored in sum
    if (X == 0):
        return 1

    ans = 0

    # If already commputed
    if (dp[X] != -1):
        return dp[X]

    # Count different no of paths
    # using all possible ways
    for i in range(1, min(X, n) + 1):
        ans = ans + findTotalPath(X - i, n, dp) % mod;
        ans %= mod;

    # Return total no of paths
    dp[X] = ans
    return ans


# Driver Code
if __name__ == '__main__':
    n = 3
    X = 2

    # Stores the number of ways
    # to obtains sums 0 to X
    dp = [-1] * (X + 1)

    # Function call
    print(findTotalPath(X, n, dp))
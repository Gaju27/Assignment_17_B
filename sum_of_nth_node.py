# Sum of nodes in the path from root to N-th node in given Tree
# Given an integer N which needs to be present as a value in a node in the last level of a Tree rooted at 1 having nodes numbered from root to the last level by increments of 1. The nodes at every odd level contain 2 children and nodes at every even level contains 4 children. The task is to find the sum of node values in the path from the root to the node N.
#
#
# Input: N = 124
# Output: 193
# Explanation: The traversal from root 1 to node 124 is 1 -> 2 -> 6 -> 16 -> 44 -> 124. Therefore, sum of all nodes in the path = 1 + 2 + 6 + 16 + 44 + 124 = 193.

# Python3 program for the above approach
from bisect import bisect_left, bisect


# Function to find sum of all
# nodes from root to N
def sumOfPathNodes(N):
    # If N is equal to 1
    if (N == 1):
        return 1

    # If N is equal to 2 or 3
    elif (N == 2 or N == 3):
        return N + 1

    # Stores the number of
    # nodes at (i + 1)-th level
    arr = []
    arr.append(1)

    # Stores the number of nodes
    k = 1

    # Stores if the current
    # level is even or odd
    flag = True

    while (k < N):

        # If level is odd
        if (flag == True):
            k *= 2
            flag = False

        # If leve is even
        else:
            k *= 4
            flag = True

        # If level with
        # node N is reached
        if (k > N):
            break

        # Push into vector
        arr.append(k)

    lenn = len(arr)
    prefix = [0] * (lenn)
    prefix[0] = 1

    # Compute prefix sums of count
    # of nodes in each level
    for i in range(1, lenn):
        prefix[i] = arr[i] + prefix[i - 1]

    it = bisect_left(prefix, N)

    # Stores the level in which
    # node N s present
    ind = it

    # Stores the required sum
    final_ans = 0
    temp = N

    while (ind > 1):
        val = temp - prefix[ind - 1]

        if (ind % 2 != 0):
            temp = prefix[ind - 2] + (val + 1) // 2
        else:
            temp = prefix[ind - 2] + (val + 3) // 4

        ind -= 1

        # Add temp to the sum
        final_ans += temp

    final_ans += (N + 1)

    return final_ans


# Driver Code
if __name__ == '__main__':
    N = 13

    # Function Call
    print(sumOfPathNodes(N))
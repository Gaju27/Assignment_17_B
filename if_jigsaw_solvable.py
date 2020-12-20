# Check whether jigsaw puzzle solveable or not
# Given a special Jigsaw puzzle consisting of N rows and M columns all identical pieces.
# Every piece has three tabs and one blank.
# The task is to check if the puzzle is solvable by placing the pieces in such a way that
# the tab of one piece fits perfectly into a blank of other piece.
#
# Input: N = 2, M = 2
# Output: Yes
#
# Input: N = 1, M = 3
# Output: Yes
# Approach: The key observation in the problem is that:
#
# If the Puzzle has only one row or only one column. Then it is possible to solve the puzzle by placing a blank tab on that shared side itself.
# If the Puzzle has two rows and two columns. Then The puzzle is solvable by placing the blank Tabs in a circular chain.
# Otherwise, It is not possible to solve the Puzzle.
# Below is the implementation of the above approach:

def checkSolveable(n, m):
    # Base Case
    if n == 1 or m == 1:
        print("YES")

    # By placing the blank tabs
    # as a chain
    elif m == 2 and n == 2:
        print("YES")
    else:
        print("NO")


# Driver Code
if __name__ == "__main__":
    n = 1
    m = 3
    checkSolveable(n, m)
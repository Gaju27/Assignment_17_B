# Area of the largest rectangle formed by lines parallel to X and Y axis from given set of points
#
# Given an array arr[] consisting of N pair of integers representing coordinates of N points, the task is to find the area of the largest rectangle formed by straight lines drawn parallel to X and Y-axis rom given set of point
#
# Input: arr[] = {{0, 0}, {1, 1}}
# Output: 1
# Explanation: The area of the largest rectangle is 1 formed by the coordinates (0, 0), (0, 1), (1, 0), (1, 1).
#
# Input: arr[] = {{-2, 0}, {2, 0}, {4, 0}, {4, 2}}
# Output: 8
# Explanation: The area of the largest rectangle possible is 8 ( length = 4 and breadth = 2 ) by the coordinates (-2, 0), (2, 0), (2, 2), (-2, 2).


# Python3 program for the
# above approach

# Function to return the
# area of the largest
# rectangle formed by lines
# parallel to X and Y axis
# from given set of points
def maxRectangle(sequence, size):
    # Initialize two arrays
    X_Cord = [0] * size
    Y_Cord = [0] * size

    # Store x and y coordinates
    for i in range(size):
        X_Cord[i] = sequence[i][0]
        Y_Cord[i] = sequence[i][1]

    # Sort arrays
    X_Cord.sort()
    Y_Cord.sort()

    # Initialize max differences
    X_Max = 0
    Y_Max = 0

    # Find max adjacent differences
    for i in range(size - 1):
        X_Max = max(X_Max,
                    X_Cord[i + 1] -
                    X_Cord[i])
        Y_Max = max(Y_Max,
                    Y_Cord[i + 1] -
                    Y_Cord[i])

    # Return answer
    return X_Max * Y_Max


# Driver Code
if __name__ == "__main__":
    # Given points
    point = [[-2, 0], [2, 0],
             [4, 0], [4, 2]]

    # Total points
    n = len(point)

    # Function call
    print(maxRectangle(point, n))
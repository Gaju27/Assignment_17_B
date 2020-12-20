# Check if given point lies in range of any of the given towers
# Input: arr[][] = { {1, 1, 3}, {10, 10, 5}, {15, 15, 15} }, X = 5, Y = 5
# Output: True
# Explanation:
# Distance of point(5, 5) from (arr[0][0], arr[0][1]) = 5.65685 and the range of first tower is 3. Therefore, the point(X, Y) does not lie in the network-range of the first tower.
# Distance of point(5, 5) from (arr[1][0], arr[1][1]) = 7.07107 and the range of second tower is 5. Therefore, the point(X, Y) does not lie in the network-range of the second tower.
# Distance of point(5, 5) from (arr[2][0], arr[2][1]) = 14.1421 and the range of third tower is 15. Therefore, the point(X, Y) lies in the network-range of the third tower.
# Since, point (X, Y) lies in the range of the third tower. Therefore, the required output is True.
#
# Input: arr[][] = { {1, 1, 3}, {10, 10, 3}, {15, 15, 3} }, X = 5, Y = 5
# Output: False

from math import sqrt


# Function to check if the point (X, Y)
# exists in the towers network-range or not
def checkPointRange(arr, X, Y, N):
    # Traverse the array arr[]
    for i in range(N):

        # Stores distance of the
        # point (X, Y) from i-th tower
        dist = sqrt((arr[i][0] - X) *
                    (arr[i][0] - X) +
                    (arr[i][1] - Y) *
                    (arr[i][1] - Y))

        # If dist lies within the
        # range of the i-th tower
        if (dist <= arr[i][2]):
            return True

    # If the point (X, Y) does not lie
    # in the range of any of the towers
    return False


# Driver Code
if __name__ == '__main__':

    arr = [[1, 1, 3],
           [10, 10, 3],
           [15, 15, 15]]
    X = 5
    Y = 5

    N = len(arr)

    # If point (X, Y) lies in the
    # range of any of the towers
    if (checkPointRange(arr, X, Y, N)):
        print("True")

    # Otherwise
    else:
        print("False")
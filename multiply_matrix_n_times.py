# Print Matrix after multiplying Matrix elements N times
#
# Input: mat[][] = {{1, 2, 3}, {3, 4, 5}, {6, 7, 9}}, N = 2
# Output:
# 25 31 40
# 45 57 74
# 81 103 134
#
# Input: mat[][] = {{1, 2}, {3, 4}}, N = 3
# Output:
# 37 54
# 81 118


# Python3 program for the above approach

# Function for matrix multiplication
def power(I, a, rows, cols):
    # Stores the resultant matrix
    # after multiplying a[][] by I[][]
    res = [[0 for i in range(cols)]
           for j in range(rows)]

    # Matrix multiplication
    for i in range(0, rows):
        for j in range(0, cols):
            for k in range(0, rows):
                res[i][j] += a[i][k] * I[k][j]

    # Updating identity element
    # of a matrix
    for i in range(0, rows):
        for j in range(0, cols):
            I[i][j] = res[i][j]


# Function to print the given matrix
def prints(a):
    # Traverse the row
    for i in range(0, len(a)):

        # Traverse the column
        for j in range(0, len(a[0])):
            print(a[i][j], end=' ')

        print()


# Function to multiply the given
# matrix N times
def multiply(arr, N):
    # Identity element of matrix
    I = [[1 if i == j else 0 for i in range(
        len(arr))] for j in range(
        len(arr[0]))]

    # Multiply the matrix N times
    for i in range(1, N + 1):
        power(I, arr, len(arr), len(arr[0]))

    # Update the matrix arr[i] to
    # to identity matrix
    for i in range(0, len(arr)):
        for j in range(0, len(arr[0])):
            arr[i][j] = I[i][j]

    # Print the matrix
    prints(arr)


# Driver Code
if __name__ == '__main__':
    # Given 2d array
    arr = [[1, 2, 3],
           [3, 4, 5],
           [6, 7, 9]]

    # Given N
    N = 2

    # Function Call
    multiply(arr, N)
# Possible arrangement of persons waiting to sit in a hall
#
# Given an integer N, a binary string S and an array W[]. S denotes the sequence of N * 2 persons entering the hall, where 0 denotes a boy and 1 denotes a girl. W[] denotes the width of seats in each row, where each row consists of exactly 2 seats. The task is to find a possible arrangement of the persons entering the hall such that following conditions are satisfied:
#
# A boy chooses a row in which both seats are empty. Among all such rows, he chooses the one with the minimum width.
# A girl chooses a row in which one seat is occupied by a boy. Among all such rows, she chooses the one with the maximum width.


# Python3 program for the above approach

# Function to find the arrangement
# of seating
def findTheOrder(arr, s, N):
    # Stores the row in which the
    # ith person sits
    ans = []

    # Stores the width of seats along
    # with their index or row number
    A = [[] for i in range(N)]

    for i in range(N):
        A[i] = [arr[i], i + 1]

    # Sort the array
    A = sorted(A)

    # Store the seats and row for
    # boy's seat
    q = []

    # Stores the index of row upto
    # which boys have taken seat
    index = 0

    # Iterate the string
    for i in range(2 * N):
        if (s[i] == '0'):

            # Push the row number at
            # index in vector and heap
            ans.append(A[index][1])
            q.append(A[index])

            # Increment the index to let
            # the next boy in the next
            # minimum width vacant row
            index += 1

        # Otherwise
        else:

            # If girl then take top of
            # element of the max heap
            ans.append(q[-1][1])

            # Pop from queue
            del q[-1]

        q = sorted(q)

    # Print the values
    for i in ans:
        print(i, end=" ")


# Driver Code
if __name__ == '__main__':
    # Given N
    N = 3

    # Given arr[]
    arr = [2, 1, 3]

    # Given string
    s = "001011"

    # Function Call
    findTheOrder(arr, s, N)
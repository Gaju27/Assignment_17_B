# Count of packets placed in each box after performing given operations
# Given two arrays arr[] and operations[] consisting of N and M integers, and an integer C. The array arr[] represents the initial number of packets in the N boxes, each of capacity C. Starting from position 1, perform the following types of operations in the sequence specified by the array operations[]:
#
# Type 1: Move to the left box.
# Type 2: Move to the right box.
# Type 3:Pick a packet from the current box.
# Type 4:Drop a packet from the current box.
# Type 5:Print the number of packets in each box and exit.
# Any operation is ignored in the following cases:
#
# Move left operation is ignored if the current position is 1.
# Move right operation is ignored if the current position is N.
# Pick a packet operation is ignored if a packet is already picked and not dropped yet or the current box is empty.
# Drop a packet operation is ignored if no packet is picked or the current box already has C packets

#
# Approach: The idea is to assign variables for each task such that for the current index, initialize curr with 0. To check if the element is picked, initialize picked with false. Follow the steps below to solve the problem:
#
# Keep a boolean variable picked to keep track if some packet has already been picked.
# If the operation type is 1 and curr is not 0, move to the left, decrementing curr by 1.
# If the operation type is 2 and curr is not (N – 1), move to the right, incrementing current curr by 1.
# If the operation type is 3 and picked is false and the current box is not empty, decrease the packet by 1 in the current box and mark picked as true.
# If the operation type is 4 and picked is true and the current box is not full, increase the packet by 1 in the current box and mark picked as false.
# If the operation type is 5, print the current values in the array arr[] and exit.


# Python3 program for the above approach

# Function to print final array after
# performing all the operations
def printFinalArray(a, n,
                    operations, p, capacity):
    # Initialize variables
    curr = 0
    picked = False

    # Traverse through all operations
    for i in range(p):

        # Operation Type
        s = operations[i]
        flag = False

        # Move left
        if (curr != 0):
            curr -= 1
            break

        # Move right
        if (curr != n - 1):
            curr += 1
            break

        # Pick a packet
        if (picked == False
                and a[curr] != 0):
            picked = True
            a[curr] -= 1
            break

        # Drop a packet
        if (picked == True
                and a[curr] != capacity):
            picked = False
            a[curr] += 1
            break

        # Exit
        else:
            flag = True

        if (flag == True):
            break

    # Print final array
    for i in range(n):
        print(a[i], end=" ")


# Driver Code
if __name__ == "__main__":
    # Given capacity
    capacity = 5

    # Given array with initial values
    a = [2, 5, 2]

    # Array size
    N = len(a)

    # Operations
    operations = [3, 2, 4, 1, 4, 5]

    # Number of operations
    M = len(operations)

    # Function call
    printFinalArray(a, N, operations,
                    M, capacity)
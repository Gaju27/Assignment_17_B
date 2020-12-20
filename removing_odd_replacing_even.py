# Find the winner of the Game of removing odd or replacing even array elements
# Given an array arr[] consisting of N integers. Two players, Player 1 and Player 2, play turn-by-turn in which one player can may either of the following two moves:
#
# Convert even array element to any other integer.
# Remove odd array element.
# The player who is not able to make any move loses the game. The task is to print the winner of the game. Print -1 if the game may go on forever.


# Python3 program for the above approach

# Function to evaluate the
# winner of the game
def findWinner(arr, N):
    # Stores count of odd
    # array elements
    odd = 0

    # Stores count of even
    # array elements
    even = 0

    # Traverse the array
    for i in range(N):

        # If arraay element is odd
        if (arr[i] % 2 == 1):
            odd += 1

        # Otherwise
        else:
            even += 1

    # If count of even is zero
    if (even == 0):

        # If count of odd is even
        if (odd % 2 == 0):
            print("Player 2")

        # If count of odd is odd
        elif (odd % 2 == 1):
            print("Player 1")

    # If count of odd is odd and
    # count of even is one
    elif (even == 1 and odd % 2 == 1):
        print("Player 1")

    # Otherwise
    else:
        print(-1)


# Driver code
if __name__ == '__main__':
    arr = [3, 1, 9, 7]
    N = len(arr)

    findWinner(arr, N)
# Minimum jumps required to make a group of persons sit together
#
# Given a string S of length N consisting of ‘x’ and ‘.’. The given string represents a row of seats where ‘x’ and ‘.’ represent occupied and unoccupied seats respectively. The task is to minimize the total number of hops or jumps to make all the occupants sit together i.e., next to each other, without having any vacant seat between them.
# Note: Since the count of jumps can be very large, print the answer modulo 109 + 7.

#Python3 program for the above approach
MOD = 10 ** 9 + 7


# Function to find the minimum jumps
# required to make the whole group
# sit adjacently
def minJumps(seats):
    # Store the indexes
    position = []

    # Stores the count of occupants
    count = 0

    # Length of the string
    lenn = len(seats)

    # Traverse the seats
    for i in range(lenn):

        # If current place is occupied
        if (seats[i] == 'x'):
            # Push the current position
            # in the vector
            position.append(i - count)
            count += 1

    # Base Case:
    if (count == lenn or count == 0):
        return 0

    # The index of the median element
    med_index = (count - 1) // 2

    # The value of the median element
    med_val = position[med_index]

    ans = 0

    # Traverse the position[]
    for i in range(len(position)):
        # Update the ans
        ans = (ans % MOD +
               abs(position[i] - med_val)
               % MOD) % MOD

    # Return the final count
    return ans % MOD


# Driver Code
if __name__ == '__main__':
    # Given arrange of seats
    S = "....x..xx...x.."

    # Function Call
    print(minJumps(S))
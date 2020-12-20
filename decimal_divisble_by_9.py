# Check if decimal representation of Binary String is divisible by 9 or not
# Input: S = 1010001
# Output:Yes
# Explanation: The decimal representation of the binary string S is 81, which is divisible by 9. Therefore, the required output is Yes.
#
# Input: S = 1010011
# Output: No
# Explanation: The decimal representation of the binary string S is 83, which is not divisible by 9. Therefore, the required output is No.

# Python3 program to implement
# the above approach

# Function to convert the binary
# string into octal representation
def ConvertequivalentBase8(S):
    # Stores binary representation of
    # the decimal value [0 - 7]
    mp = {}

    # Stores the decimal values
    # of binary strings [0 - 7]
    mp["000"] = '0'
    mp["001"] = '1'
    mp["010"] = '2'
    mp["011"] = '3'
    mp["100"] = '4'
    mp["101"] = '5'
    mp["110"] = '6'
    mp["111"] = '7'

    # Stores length of S
    N = len(S)

    if (N % 3 == 2):

        # Update S
        S = "0" + S

    elif (N % 3 == 1):

        # Update S
        S = "00" + S

    # Update N
    N = len(S)

    # Stores octal representation
    # of the binary string
    octal = ""

    # Traverse the binary string
    for i in range(0, N, 3):

        # Stores 3 consecutive characters
        # of the binary string
        temp = S[i: i + 3]

        # Append octal representation
        # of temp
        if temp in mp:
            octal += (mp[temp])

    return octal


# Function to check if binary string
# is divisible by 9 or not
def binString_div_9(S, N):
    # Stores octal representation
    # of S
    octal = ConvertequivalentBase8(S)

    # Stores sum of elements present
    # at odd positions of oct
    oddSum = 0

    # Stores sum of elements present
    # at odd positions of oct
    evenSum = 0

    # Stores length of oct
    M = len(octal)

    # Traverse the string oct
    for i in range(0, M, 2):
        # Update oddSum
        oddSum += ord(octal[i]) - ord('0')

    # Traverse the string oct
    for i in range(1, M, 2):
        # Update evenSum
        evenSum += ord(octal[i]) - ord('0')

    # Stores cotal representation
    # of 9
    Oct_9 = 11

    # If absolute value of (oddSum
    # - evenSum) is divisible by Oct_9
    if (abs(oddSum - evenSum) % Oct_9 == 0):
        return "Yes"

    return "No"


# Driver Code
if __name__ == "__main__":
    S = "1010001"
    N = len(S)

    print(binString_div_9(S, N))
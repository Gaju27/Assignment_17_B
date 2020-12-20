# Numbers formed by flipping common set bits in two given integers
#
# Input: A = 7, B = 4
# Output: 3 0
# Explanation:
# The binary representation of 7 is 111
# The binary representation of 4 is 100
# Since the 3rd bit of both A and B is a set bit. Therefore, flipping the 3rd bit of A and B modifies A = 3 and B = 0
# Therefore, the required output is 3 0
#
# Input: A = 10, B = 20
# Output: 10 20

# Function to flip bits of A and B
# which are set in both of them
def flipBitsOfAandB(A, B):
    # Iterate all possible bits of
    # A and B
    for i in range(0, 32):

        # If ith bit is set in
        # both A and B
        if ((A & (1 << i)) and
                (B & (1 << i))):
            # Clear i-th bit of A
            A = A ^ (1 << i)

            # Clear i-th bit of B
            B = B ^ (1 << i)

    print(A, B)


# Driver Code
if __name__ == "__main__":
    A = 7
    B = 4

    flipBitsOfAandB(A, B)


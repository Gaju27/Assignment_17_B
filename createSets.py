# program to Split N natural numbers into two sets having GCD of their sums greater than 1
def createSets(N):
   
    # No such split
    # possible for N <= 2
    if (N <= 2):
        print("-1");
        return;
 
    # Print the first set
    # consisting of even elements
    for i in range(2, N + 1, 2):
        print(i, end=" ");
    print("");
 
    # Print the second set
    # consisting of odd ones
    for i in range(1, N + 1, 2):
        print(i, end = " ");
 
# Driver Code
if __name__ == '__main__':
    N = 6;
    createSets(N);
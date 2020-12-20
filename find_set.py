# Program to Partition first N natural number into two sets such that their sum is not coprime
def find_set(n): 
  
    # Impossible case 
    if (n <= 2): 
        print("-1"); 
        return; 
  
    # Sum of first n-1 natural numbers 
    sum1 = (n * (n - 1)) / 2; 
    sum2 = n; 
    print(sum1, " ", sum2); 
  
# Driver code 
n = 8; 
find_set(n); 
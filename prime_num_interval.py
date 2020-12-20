# Program to display all the prime numbers within an interval

def prime_num_interval(lower,upper):
    for num in range(lower, upper + 1):
       # all prime numbers are greater than 1
       if num > 1:
           for i in range(2, num):
               if (num % i) == 0:
                   break
           else:
               return (num)
            
print(prime_num_interval(10,50))
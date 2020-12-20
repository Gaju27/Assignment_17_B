#  Program to check Armstrong numbers in a certain interval

def armstrong_number_interval(lower,upper):
    for num in range(lower, upper + 1):

       # order of number
       order = len(str(num))

       # initialize sum
       sum = 0

       temp = num
       while temp > 0:
           digit = temp % 10
           sum += digit ** order
           temp //= 10

       if num == sum:
           print(num)
            
print(armstrong_number_interval(100,1500))
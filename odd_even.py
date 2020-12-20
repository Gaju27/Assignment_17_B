# program to check if the number is an Armstrong number or not
def armstrong_num_or_not(num):
    sum = 0
    temp = num
    while temp > 0:
       digit = temp % 10
       sum += digit ** 3
       temp //= 10

    # display the result
    if num == sum:
       return f"{num} is an Armstrong number"
    else:
       return f"{num} is not an Armstrong number"
    
print(armstrong_num_or_not(262))
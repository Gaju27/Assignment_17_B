# Find list of number are divisible by another given number
def divisible_number(n,list_input):
    return list(filter(lambda x: (x % n == 0), list_input))

print(divisible_number(4,[1,3,4,16]))
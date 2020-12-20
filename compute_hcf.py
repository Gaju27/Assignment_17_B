# Compute HCF of two numbers
def compute_hcf(x, y):

# choose the smaller number
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i 
    return hcf

num1 = 20 
num2 = 24

print("Thecompute HCF for two numbers: ", compute_hcf(num1, num2))

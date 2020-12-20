#Use Euclid’s division algorithm to find the HCF of two numbers:

def euclids_hcf(x, y):
   while(y):
       x, y = y, x % y
   return x

hcf = euclids_hcf(30, 400)
print("euclids_hcf: ", hcf)
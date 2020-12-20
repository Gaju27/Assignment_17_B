# Multiplication table generator

def multi_table(input):
    for i in range(1,11):
        print (f'{input} X {i} = {input * i}')
    
multi_table(10)
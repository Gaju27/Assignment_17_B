# Convert Decimal to Hexadeicmal,binary,Octal
def decimal_to(numb,type1):
    if type1== 'hexa':
        return hex(numb)
    elif type1== 'binary':
        return bin(numb)
    elif type1 == 'oct':
        return oct(numb)
    else:
        return numb
    
print(decimal_to(10,'oct'))
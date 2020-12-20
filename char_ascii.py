# character to ASCII and vice versa
def char_ascii(input,value='ascii'):
    if value=='ascii':
        return chr(input)
    elif value == 'ord':
        return ord(input)

print(char_ascii(65))
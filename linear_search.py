# Python program to do linear search in a list
def linear_search(arr, x): 
    for i in range(0, len(arr)): 
        if (arr[i] == x): 
            return i 
    return -1

print('leanear search for list',linear_search([12, 3, 5, 7, 19,23,2], 2)) 
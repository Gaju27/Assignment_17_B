#program to check palindrome or not
 
def isPalindrome(s):
    return s == s[::-1]

print(isPalindrome('malayalam'))
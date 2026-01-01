s=input("enter a string:")

def check_palindrome(s):
    res=""
    for i in range(len(s)):
        res=s[i]+res
    if res==s:
        return True
    else:
        return False
print(check_palindrome(s))
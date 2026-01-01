s=input("enter a string:")
def palindrome(s):
    i=0
    j=len(s)-1
    while i<j:
        if s[i]!=s[j]:
            return "Not a Palindrome"
        i+=1
        j-=1
    return "Palindrome"
print(palindrome(s))
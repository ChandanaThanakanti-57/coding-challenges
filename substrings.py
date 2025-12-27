s=input('enter a string to find substrings:')
ans=""
def substring(s,ans):

    if len(s)==0:
        print(ans)
        return 
    substring(s[1:],ans+s[0])#include case
    substring(s[1:],ans)#exclude
print(substring(s,ans))
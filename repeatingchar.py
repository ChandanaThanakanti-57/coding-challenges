#find first non repeative character
s=input('enter a string:')
def helper(s):
    for char in s:
        if s.count(char)==1:
            return char
    return "no repeating character"
print(helper(s))
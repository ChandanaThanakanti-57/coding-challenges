#remove duplicates in a string
s=input('enter a string:')
res=""
for char in s:
    if char not in res:
        res+=char
print(res)
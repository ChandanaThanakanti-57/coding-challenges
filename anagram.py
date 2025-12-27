s=input('enter string1:')
r=input('enter string2:')
res={}
res1={}
for char in s:
    res[char]=res.get(char,0)+1
for char in r:
    res1[char]=res1.get(char,0)+1
def anagram(res,res1):
    if len(res)!=len(res1):
        return "not an anagram"
    for char in res:
        if res[char]!=res1.get(char,0):
            return "not an anagram"
    return "anagram"
print(anagram(res,res1))
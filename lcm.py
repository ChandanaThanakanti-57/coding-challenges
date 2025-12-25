n=int(input('enter n value:'))
m=int(input('enter m value:'))
res=0
a=n
b=m
while n!=0 and m!=0:
    if n>m:
        n=n%m
    else:
        m=m%n
if n!=0:
    res=n
else:
    res=m
print(a*b/(res))

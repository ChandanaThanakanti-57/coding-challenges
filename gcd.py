n=int(input('enter n value:'))
m=int(input('enter m value:'))
if n>m:
    x=m
else:
    x=n
def gcd(n,m,x):
    for i in range(x,0,-1):
        if n%i==0 and m%i==0:
            return i
print(f'gcd of {n},{m} is {gcd(n,m,x)}')
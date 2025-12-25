n=int(input('enter n value:'))
if n<=1:
    print('not a prime number')
for i in range(2,n):
    if n%i==0:
        print(f"{n} not a prime number")
else:
    print(f'{n} is a prime number')
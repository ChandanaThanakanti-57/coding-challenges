n=int(input('enter n value: '))
for i in range(1,n+1):
    for k in range(n-i):
        print(' ',end='')
    for j in range(i):
        print('*',end='')
    print()

for i in range(1,n+1):
    for k in range(i):
        print(' ',end='')
    for j in range(n-i):
        print('*',end='')
    print()

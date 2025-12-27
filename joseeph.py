n=int(input('enter n value:'))
k=int(input('enter k value:'))
def joseeph(n,k):
    if n==1:
        return 0
    return (joseeph(n-1,k)+k)%n
print(joseeph(n,k))
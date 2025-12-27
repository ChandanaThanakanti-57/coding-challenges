#recursion
n=int(input('enter n value:'))
def helper(n):
    print(n)
    if n >= 5:
        return
    helper(n + 1)

helper(n)
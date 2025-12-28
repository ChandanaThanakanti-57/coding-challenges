def combinations(n,k,curr,start):
    if len(curr)==k:
        print(curr)
        return
    for j in range(start,n+1):
        curr.append(j)
        combinations(n,k,curr,j+1)
        curr.pop()
combinations(4,2,[],1)
        


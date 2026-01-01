s=[0,0,1,1,1,0,0,1,1,1,1,0]
max=0
count=0
for num in s:
    if num==1:
        count+=1
    else:
        if count>max:
            max=count
        count=0
if count>max:
    max=count
print(max)

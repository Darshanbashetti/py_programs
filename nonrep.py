a=[3,4,1,2,3,1,4,5,6,7,8,9,8,7,6,4,2,3,5,0,1]
b=[]
for i in a:
    a.remove(i)
    if i not in a:
        b.append(i)

print(b)
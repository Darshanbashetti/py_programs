a=[1,3,5,7,9]
b=[2,3,5,7,9]
c=[1,2,3,4,5,6,7,8,9]

d=[]

for i in a:
    if i in b:
        if i in c:
            d.append(i)

print(d)
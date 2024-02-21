a=[1,0,2,0,1,2,1,2,1,0,1,2]
b=[]
for i in a:
    if i==0:
        b.append(i)
for i in a:
    if i==1:
        b.append(i)

for i in a:
    if i==2:
        b.append(i)
print(b)
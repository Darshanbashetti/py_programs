m=[1,7,3,6,2,8,9,4,3,]
n=len(m)
for i in range(n):
    for j in range(i+1,n):
        if m[i]>m[j]:
            m[i],m[j]=m[j],m[i]
print(m)

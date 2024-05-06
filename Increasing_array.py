a=int(input())
b=input().split(' ')

x=c=0
while x<a-1:
    if int(b[x]) > int(b[x+1]):
        c+=int(b[x])-int(b[x+1])
        b[x+1]=b[x]
    x+=1
print(c)
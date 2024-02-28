n=int(input("Enter digit : "))
s=str(n)
a=0
b=0
for i in s:
    if a==0:
        a=i
        break
for i in s:
    b=(i)+str(b)
for i in str(b):
    b=i
    break
print(int(a)+int(b))
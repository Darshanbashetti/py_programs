l=[]
n=int(input("Numbers : "))
for i in range(0,n):
    l.append(int(input()))
small=l[0]
large=l[0]

for i in l:
    if i<small:
        small=i
    if i>large:
        large=i
print("Smallest number is ",small)
print("Largest number is",large)
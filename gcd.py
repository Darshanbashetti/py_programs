'''a = int(input("Enter a : "))
b = int(input("Enter b : "))

if a%2==0 and b%2==0:
    print("2")
else:
    for i in range(1,a+1 or b+1):
'''
a = int(input("Enter a : "))
b = int(input("Enter b : "))
res = a*b
if a > b:
    max = a
else:
    max = b

while(True):
    if(max % a == 0 and max % b == 0):
        lcm = max
        break
    max += 1
print(res/lcm)

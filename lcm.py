'''from termios import NL1


a = int(input("Enter a : "))
b = int(input("Enter b : "))
lcm = 1
if a/2 == 0 and b/2 == 0:
    lcm = a*b
    print(lcm)
else:
    if a < b:
        b *= 2
        print(b)
    else:
        a *= 2
        print(a)
'''

# correct one
a = int(input("Enter a : "))
b = int(input("Enter b : "))

if a > b:
    max = a
else:
    max = b

while(True):
    if(max % a == 0 and max % b == 0):
        lcm = max
        break
    max += 1

print(lcm)

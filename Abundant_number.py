n = int(input("Enter a number to check if its a Abundant number :   "))
m = 0
for i in range(1, n):
    if n % i == 0:
        m = m+i
if m > n:
    print(n, "is Abundant number ")
else:
    print("NO")

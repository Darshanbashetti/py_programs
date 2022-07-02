'''
n = int(input("enter a number to find its factorail : "))
fact = 1
if n == 0 or n == 1:
    print("1")
else:
    for i in range(2, n+1):
        fact = fact*i
print(fact)


# with inbuild function
print(factorial(n))
'''
# recursion
n = int(input("enter :"))


def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*fact(n-1)


print(fact(n))

n = int(input("enter range :"))


def fib(n):
    if n <= 0:
        print("give postive number as input : ")
    else:
        a = 0
        b = 1
        if n == 1:
            print(a)
        else:
            print(a)
            print(b)
            for i in range(2, n):
                c = a+b
                a = b
                b = c
                print(c)


fib(n)

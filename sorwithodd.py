# # remove all even and sort the array
# n=int(input())
# a=[]
# for i in range(1,n+1):
#     b=int(input())
#     a.append(b)
# for i in a:
    

n = int(input())
a = []

for i in range(n):
    b = int(input())
    a.append(b)

a = [x for x in a if x % 2 != 0]

a.sort()

print(a)

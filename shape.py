# # 1
# # 121
# # 12321
# # 1234321
# # 123454321

# n=int(input("SIze = "))
# m=''
# b=''
# if n>1:
#     for i in range(1,n+1):
#         m+=str(i)
# # print(m)
# for i in m:
#     if i==n:
#         break
#     else:
#         b=i+b
# c=m+b
# print(c)
        
n = int(input('Enter how many lines? '))

for i in range(1,n+1):
    for j in range(1, n+1-i):
        print(' ', end='')
    for j in range(1,i+1):
        print(j, end='')
    for j in range(i-1,0,-1):
        print(j, end='')
    print()


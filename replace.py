# n=int(input())

# for i in range(1,n):
#     if n%i==0:
#         print(i)
        
    
# replace all xeros into 1
# and 1 into 2

a='1781010101010'
b=''
for i in a:
    if i=='0':
        b=b+'1'
    elif i=='1':
        b=b+'2'
    else:
        b=b+i
print(b)

n = int(input())
def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*fact(n-1)
f=(fact(n))
s=str(f)
count=0
max=0
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        count += 1
        if max<=count:
            max=count
    elif s[i]!=s[i+1]:
        count=0
print(max+1)

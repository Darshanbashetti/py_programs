# Question:
# Write a program that takes two integers, n1 and n2, as input and prints the first y common multiples of n1 and n2.

# Example:
# Input: n1 = 3, n2 = 5, y = 4
# Output: 15, 30, 45, 60

n1=int(input("1st : "))
n2=int(input("2nd : "))
y=int(input("Multiples : "))
n1ans=[]
n2ans=[]
ans=[]

if n1<1 and n2<1:
    print("Invalid")
elif y<1:
    print("Invalid")
else:
    for i in range(1,50):
        n1ans.append(n1*i)
        n2ans.append(n2*i)

for i in n1ans:
    if i in n2ans:
        ans.append(i)

for i in range(1,y+1):
    print(ans[i])
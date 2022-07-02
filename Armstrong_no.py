num = int(input("Enter a number to check if it is a Armstrong number or not : "))
n = len(str(num))
sum = 0
temp = num
while num > 0:
    digit = num % 10
    sum += digit**n
    num = num//10
if sum == temp:
    print("Armstrong")
else:
    print("not an Armstrong ")

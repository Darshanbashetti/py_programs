no = int(input("Enter the number of patients : "))
ages = []
fees = 0
for i in range(0, no):
    user_input = int(input("Enter age : "))
    if int(user_input) == 0:
        break
    elif user_input > 0 and user_input < 120:
        ages.append(user_input)
    else:
        print("age insaan ka daal bhai")
for i in ages:
    if i <= 17:
        fees += 200
    elif i <= 40:
        fees += 400
    else:
        fees += 300
print("Total Income ", fees, " INR")

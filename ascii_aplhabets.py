# ascii value for letters

user_input = input("enter : ")
print(ord(user_input))


# ascii value for a word

user_input2 = input("enter a word :")
for i in range(0, len(user_input2)):
    print(user_input2[i], "=", ord(user_input2[i]))


# ascii value for a word in reverse way

user_input3 = input("Enter a word :")
for i in range(0, len(user_input3)):
    print(user_input3[i], '=', ord(user_input3[i]))

rev = user_input3[::-1]
print(rev)

for j in range(0, len(rev)):
    print(user_input3[j], '=', ord(user_input3[j]))

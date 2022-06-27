'''from pickletools import string1


string = input("enter a string : ")
print(string)
for i in range(0, len(string)):
    print(string[i].swapcase(), end='')


'''
user_input = input("enter a string:")
String1 = str()
for i in user_input:
    if i.isupper():
        i = i.lower()
        String1 = String1 + i
    else:
        i = i.upper()
        String1 = String1 + i
print(user_input + ' after changing ' + String1)

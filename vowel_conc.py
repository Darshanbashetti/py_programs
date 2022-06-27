
ip = str(input("Enter a string to check wether it is a vowel or consonent : "))
if not ip.isalpha():
    print("not charector")
elif(ip == 'a' or ip == 'e' or ip == 'i' or ip == 'o' or ip == 'u'):
    print("vowel")
else:
    print("consonents")


# with using classes
c = input("Enter a charector : ")


def lower(c):
    return c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u'


def capital(c):
    return c == "a" or c == "e" or c == "i" or c == "o" or c == "u"


if not c.isalpha():
    print("Non alphabet")
elif lower(c) or capital(c):
    print(c, "is a Vowel")
else:
    print(c, "is a consonant")

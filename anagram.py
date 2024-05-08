a=input()
b=input()

if len(a)!=len(b):
    print("not an anagram")
else:
    for i in a:
        if i not in b:
            print("Not an anagram")
            break
        else:
            continue
    else:
        print("Anagram")    
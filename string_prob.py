# Enter your code here. Read input from STDIN. Print output to STDOUT
s = input()
while 1:
    i=0
    flag=0
    while i<len(s)-1:
        if s[i] == s[i+1]:
            s=s[:i]+s[i+2:]
            flag=1
        else:    
            i+=1
    if flag==0:
        break
if len(s)>0:        
    print(s)        
else:
    print('Empty String')
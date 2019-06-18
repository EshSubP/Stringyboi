st,l=' ',[ ]
S = input("Enter the String : ")
l = S.split(';')
for x in l:
    a=tuple(x.split('='))
    b=l.append(str(a))    
print(b)    

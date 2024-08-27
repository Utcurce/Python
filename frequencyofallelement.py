a=input('Enter the string->')
b=len(a)
for i in range(0,b):
    c=a[i]
    print(f'{c} =',a.count(c))

a=int(input('Enter the number->'))
k=0
s=1
for i in range(1,a+1):
    if (a%s==0):
        k=k+1
    s=s+1
if k==2:
    print(f'{a} is a prime number')
else:
    print(f'{a} is not a prime number')

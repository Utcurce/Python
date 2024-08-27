a=int(input('Enter the number:'))
if (a%3==0 and a%7==0):
    print(f'{a} is divisible by both 3 and 7')
elif a%3==0:
    print(f'{a} is divisible by 3')
elif a%7==0:
    print(f'{a} is divisible by 7')
else:
    print(f'{a} is divisible by none')

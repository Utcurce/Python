##num = int(input("Enter a number"))
##if num == num[::-1]:
##    print("Yes its a palindrome")
##else:
##    print("No, its not a palindrome")
num=int(input('Enter the number->'))
s=0
a=num
while a>0:
    x=a%10
    s=s*10+x
    a//=10
if(num==s):
    print('Palindrome')
else:
    print('Not')

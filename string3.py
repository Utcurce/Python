##a=input('Enter the string:')
##c=len(a)
##b=''
##for i in range(c,0,-1):
##    b=b+a[i-1]
##print(b)
##a=input('Enter the string:')
##count=len(a)
##b=''
##for i in range(count,0,-1):
##    b=b+a[i-1]
##if (a==b):
##    print('Given string is palindrome')
##else:
##    print('Given string is not a palindrome')
##a=input('Enter first string')
##b=input('Enter second string')
##if(a==b):
##    print('The string are same')
##else:
##    print('The string are not same')
a=int(input('Enter the number of element for 1:'))
b=int(input('Enter the number of element for 2:'))
list1=[]
list2=[]
for i in range(a):
   list1.append(input('Enter the value for 1:'))
for i in range(b):
    list2.append(input('Enter the value for 2:'))
c=list1+list2
d=tuple(c)
print(d)


















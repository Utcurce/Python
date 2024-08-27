##l=[]
##n=int(input('Enter the number of elements:'))
##for i in range(0,n,1):
##    k=input()
##    l.append(k)
##for i in range(0,n,1):
##    print(l[i])
##a=[]
##n=int(input('Enter the number of element:'))
##for i in range(0,n,1):
##    k=input(f'Enter the {i} number:')
##    a.append(k)
##for i in range(0,n,1):
##    print(a[i])
##m=max(a)
##print(m)
##mi=min(a)
##print(mi)
##l=len(a)
##print(l)
##a.sort()
##print(a)
##a.reverse()
##print(a)
##s=sum(a)
##print(s)
##############################      TUPLE       ###############################################
##t1=()
##t2=(3,)
##t3=(23,56,67,87,9)
##t4=t3+t2
##print(t4)
##############################       PATERN      ##########################################
##row=int(input('Enter the number of rows:'))
##for i in range(row):
##    for j in range(i+1):
##        print('*',end=' ')
##    print('\n')
##    if (row==i):
##        for k in range(row):
##            print('*',end='')
##        row=row-1
##############################      ARMSTRONG    ################################################
##a=int(input('Enter the number:'))
##b=len(str(a))
##sum=0
##x=a
##while a>0:
##    k=a%10
##    sum=sum+k**b
##    a=a//10
##if (sum==x):
##    print(x,'is a Armstrong number')
##else:
##    print(x,'is not Armstrong number'
##############################      PRIME    ################################################
##a=int(input('Enter the number:'))
##flag=1
##if(a==1):
##    print(a,'is not a prime number')
##elif(a>1):
##    for i in range(2,a):
##        if(a%i==0):
##            flag=0
##            break
##if(flag==1):
##    print(a,'is a prime number')
##else:
##    print(a,'is not a prime number')
##############################      PALINDROME   ################################################
##a=int(input('Enter the number:'))
##b=a
##r=0
##while(a>0):
##    d=a%10
##    r=r*10+d
##    a=a//10
##if(b==r):
##    print(b,'is a Palindrome number')
##else:
##    print(b,'is not a Palindrome number')
##############################      FACTORIAL    ################################################
##a=int(input('Enter the number:'))
##b=1
##for i in range(1,a+1):
##    b=b*i
##print(f'The factorial of the given number is:{b}')
a=[]
n=int(input('Enter the number of element:'))
for i in range(n):
    k=int(input(f'Enter the {i} element in list:'))
    a.append(k)
for i in range(n):
    if(a[i]==a[1+i]):
        a.remove(i)
print(a)





































        








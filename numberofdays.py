a=int(input('Enter the position of month:'))
x=a%2
b=(x==0)*(a<=7)*30+(x!=0)*(a<=7)*31+(a>=8)*(x!=0)*30+(a>=8)*(x==0)*31
print('No. of days in given month is',b)


##1 -> 31
##2 -> 28
##3 -> 31
##4 -> 30
##5 -> 31
##6 -> 30
##7 -> 31
##8 -> 31
##9 -> 30
##10-> 31
##11-> 30
##12-> 31

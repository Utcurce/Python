i=int(input())
n=0
j=
while n<=i:
    n=1+n
    while i==0:
        i+=1
        if(i%3==0)and (i%5==0):
            print("FizzBuzz")
        elif(i%3==0) and (i%5!=0):
            print("Fizz")
        elif(i%5==0) and (i%3!=0):
            print("Buzz")
        else:
            print(i)

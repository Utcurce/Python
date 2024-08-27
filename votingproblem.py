##a=input('Enter your name:')
##b=int(input('Enter your age:'))
##d=' is elegible to vote'
##e=' is not elegible to vote'
##c=(b>=18)*d+(b<18)*e
##print(f'{a}{c}')
a=input('Enter your name:')
b=int(input('Enter your age:'))
(b>=18) and print(f'{a} is elegible to vote')
(b<18) and print(f'{a} is not elegible to vote')

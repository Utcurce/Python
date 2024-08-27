a1=float(input('Enter the x-cordinates of center of circle:'))
a2=float(input('Enter the y-cordinates of center of circle:'))
b=float(input('Enter the radius of the circle:'))
c1=float(input('Enter the x-cordinates of arbitrary point:'))
c2=float(input('Enter the y-cordinates of arbitrary point:'))
d=(((c1-a1)**2)+((c2-a2)**2))**1/2
if d>b:
    print('Arbitrary point is outside the circle')
elif d<b:
    print('Arbitrary point is inside the circle')
else:
    print('Arbitrary point is on boundry')
    

a = int(input('Grade obtained in Geometry:'))
while a < 0 or a > 10:
    print('Invalid grade please check and re-enter:')
    a = int(input('Grade obtained in Geometry:'))

b = int(input('Grade obtained in Algebra:'))
while b < 0 or b > 10:
    print('Invalid grade please check and re-enter:')
    b = int(input('Grade obtained in Algebra:'))

c = int(input('Grade obtained in Physics:'))
while c < 0 or c > 10:
    print('Invalid grade please check and re-enter:')
    c = int(input('Grade obtained in Physics:'))

d = ( a + b + c ) / 3


if d >= 7:
    print('Your average score is',d,'. Good job')

if d <= 6 and d >= 4:
    print('Your average score is',d,'. You need to work harder.' )

if d <=4:
    print('Your average score is',d,'. Failed, you really need to work harder.')

# I don't know how to avoid the space after my float character. If you read this code then please help me by telling how.


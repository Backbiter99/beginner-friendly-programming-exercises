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

print('The average score obtained is',d)
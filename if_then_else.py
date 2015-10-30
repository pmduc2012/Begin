__author__ = 'duc'
'''
score = 80

if score >= 90:
    print('grade A')
elif score >= 80:
    print('grade B')
elif score>= 70:
    print('grade C')
elif score >= 60:
    print('grade D')
else:
    print('grade E')

'''

while True:
    height = float(input('Input height: '))
    weight = float(input('Input weight: '))

    BMI = (weight * 0.453)/((height * 0.0254) ** 2)
    print('{0:2f}'.format(BMI))

    if BMI < 18.5:
        print('Underweight')
    elif BMI <25:
        print('Normal')
    elif BMI < 30:
        print('Overweight')
    else:
        print('Obese')



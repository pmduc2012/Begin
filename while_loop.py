__author__ = 'duc'
n1 = int(input('Input first number: '))
n2 = int(input('Input seconds number: '))

k = 2
gcd = 1

if n1 == 0 or n2 == 0:
    print('0')
else:
    while k <= abs(n1) and k <= abs(n2):
        if abs(n1) % k == 0 and abs(n2) % k == 0:
            gcd = k
        k += 1

    print(gcd)
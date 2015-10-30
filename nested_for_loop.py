__author__ = 'duc'
print('\t\t\t\tMultiplication Table')
print('        ',end='')
for i in range(1, 10):
    print(i, end='    ')
print()
print('-'*50)
for j in range(1, 10):
    print('%d  |' % j, end='')
    for k in range(1,10):
        print('%5d' % (j * k), end ='')
    print()


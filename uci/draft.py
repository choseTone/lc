__author__ = 'wangqc'

for i in range(0, 128, 4):
    print(' L %X,4' % (4*i))

for i in range(127, 0, -4):
    print(' L %X,4' % (4*i + 2**12))
    print(' S %X,4' % (4*i))
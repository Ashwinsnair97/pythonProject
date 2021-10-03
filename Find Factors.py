from math import *


def factor(n):
    fac = list()
    for i in range(1, int(sqrt(n)+1)):
        if n % i == 0:
            fac.append(int(i))
            if i != (n/i):
                fac.append(int(n/i))
    return fac


num = int(input('Give number: '))
factors = factor(num)
factors.sort()
print('Factors are')

print(factors)


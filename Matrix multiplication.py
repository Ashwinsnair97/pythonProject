from numpy import *

m1 = matrix('1 2 3; 4 5 6')
m2 = matrix('10 11; 20 21')
s1 = m1.shape
s2 = m2.shape
mul = empty((s1[0], s2[1]), int)
if s1[1] == s2[0]:
    for i in range(s1[0]):
        for k in range(s2[1]):
            pr = 0
            for j in range(s1[1]):
                pr = pr + m1[i, j]*m2[j, k]
            mul[i, k] = pr
    print(mul)
    print(m1*m2)
else:
    print('not possible boi')







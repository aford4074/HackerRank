'''
Polynomials

www.hackerrank.com/challenges/np-polynomials

python 2.7

Sample Input

1.1 2 3
0

Sample Output

3.0
'''

import numpy as np

coef = map(float, raw_input().split(' '))
x = float(raw_input())

print np.polyval(coef, x)

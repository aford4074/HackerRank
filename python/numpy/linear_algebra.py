'''
Linear Algebra

www.hackerrank.com/challenges/np-linear-algebra

python 2.7

Sample Input

2
1.1 1.1
1.1 1.1

Sample Output

0.0
'''

import numpy as np

n = int(raw_input())

a = np.array([raw_input().split(' ')[:n] for _ in xrange(n)], dtype = np.float)

print np.linalg.det(a)

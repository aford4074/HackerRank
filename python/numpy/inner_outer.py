'''
Inner and Outer

www.hackerrank.com/challenges/np-inner-and-outer

python 2.7

Sample Input

0 1
2 3

Sample Output

3
[[0 0]
 [2 3]]
'''

import numpy as np

a = np.array(raw_input().split(' '), dtype = np.int)
b = np.array(raw_input().split(' '), dtype = np.int)

print np.inner(a, b)
print np.outer(a, b)

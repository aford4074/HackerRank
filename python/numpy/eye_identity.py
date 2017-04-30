'''
Eye and Identity

www.hackerrank.com/challenges/np-eye-and-identity

python 2.7

Sample Input

3 3

Sample Output

[[ 1.  0.  0.]
 [ 0.  1.  0.]
 [ 0.  0.  1.]]
'''

import numpy as np

def hackerrank(n, m):
    print np.eye(n, m, k = 0)

hackerrank(*map(int, raw_input().split(' ')))

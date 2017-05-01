'''
Min and Max

www.hackerrank.com/challenges/np-min-and-max

python 2.7

Sample Input

4 2
2 5
3 7
1 3
4 0

Sample Output

3
'''

import numpy as np

def hackerrank(a):
    print np.max(np.min(a, axis = 1))

n, m = map(int, raw_input().split(' '))
a = np.array([raw_input().split(' ')[:m] for _ in xrange(n)], dtype = np.int)

hackerrank(a)

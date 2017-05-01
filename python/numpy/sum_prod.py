'''
Sum and Prod

www.hackerrank.com/challenges/np-sum-and-prod

python 2.7

Sample Input

2 2
1 2
3 4

Sample Output

24
'''

import numpy as np

def hackerrank(a):
    print np.prod(np.sum(a, axis = 0))

n, m = map(int, raw_input().split(' '))
a = np.array([raw_input().split(' ')[:m] for _ in xrange(n)], dtype = np.int)

hackerrank(a)

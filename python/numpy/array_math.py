'''
Array Mathematics

www.hackerrank.com/challenges/np-array-mathematics

python 2.7

Sample Input

1 4
1 2 3 4
5 6 7 8

Sample Output

[[ 6  8 10 12]]
[[-4 -4 -4 -4]]
[[ 5 12 21 32]]
[[0 0 0 0]]
[[1 2 3 4]]
[[    1    64  2187 65536]]
'''

import numpy as np

def hackerrank(a1, a2):
    print a1 + a2
    print a1 - a2
    print a1 * a2
    print a1 / a2
    print a1 % a2
    print a1**a2

n, m = map(int, raw_input().split(' '))

l1 = [[r for r in raw_input().split(' ')[:m]] for _ in xrange(n)]
l2 = [[r for r in raw_input().split(' ')[:m]] for _ in xrange(n)]

a1 = np.array(l1, dtype = np.int)
a2 = np.array(l2, dtype = np.int)

hackerrank(a1, a2)

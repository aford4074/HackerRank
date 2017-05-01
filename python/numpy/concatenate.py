'''
Concatenate

www.hackerrank.com/challenges/np-concatenate

python 2.7

Sample Input

4 3 2
1 2
1 2
1 2
1 2
3 4
3 4
3 4

Sample Output

[[1 2]
 [1 2]
 [1 2]
 [1 2]
 [3 4]
 [3 4]
 [3 4]]
 '''

import numpy as np

def hackerrank(l1, l2):
    a1 = np.array(l1, int)
    a2 = np.array(l2, int)

    print np.concatenate((a1, a2), 0)

n, m, p = map(int, raw_input().split(' '))

l1 = [raw_input().split(' ')[:p] for i in xrange(n)]
l2 = [raw_input().split(' ')[:p] for i in xrange(m)]

hackerrank(l1, l2)

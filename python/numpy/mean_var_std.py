'''
Mean, Var, Std

www.hackerrank.com/challenges/np-mean-var-and-std

python 2.7

Sample Input

2 2
1 2
3 4
Sample Output

[ 1.5  3.5]
[ 1.  1.]
1.11803398875
'''

import numpy as np

n, m = map(int, raw_input().split(' '))
a = np.array([raw_input().split(' ')[:m] for _ in xrange(n)], dtype = np.int)

print np.mean(a, axis = 1)
print np.var(a, axis = 0)
print np.std(a)

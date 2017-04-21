'''
Reduce Function

Sample Input 0

3
1 2
3 4
10 6

Sample Output 0

5 8
'''

from fractions import Fraction
from functools import reduce

n = int(input())

t = reduce(lambda x, y: Fraction(x) * Fraction(y), [input().replace(' ', '/') for i in range(n)])

print(t.numerator, t.denominator)

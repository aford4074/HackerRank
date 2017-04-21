'''
Re.start() & Re.end()

www.hackerrank.com/challenges/re-start-re-end

Sample Input

aaadaa
aa

Sample Output

(0, 1)
(1, 2)
(4, 5)
'''

import re

def re_start_end(s, k):
    regex = r'(?=(%s))' % k
    m = re.finditer(regex, s)
    results = list(map(lambda l: (l.start(1), l.end(1) - 1), m))

    return results if results else [(-1, -1)]

s, k = input(), input()
print('\n'.join(map(str, re_start_end(s, k))))

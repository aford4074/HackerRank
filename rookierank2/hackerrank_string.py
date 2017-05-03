'''
HackerRank in a String!

www.hackerrank.com/contests/rookierank-2/challenges/hackerrank-in-a-string

python 2.7

Sample Input 0

2
hereiamstackerrank
hackerworld

Sample Output 0

YES
NO
'''

def hackerrank(s):
    hr = 'hackerrank'
    i = 0

    for l in s:
        if l == hr[i]:
            i += 1
            if i == 10:
                return 'YES'

    return 'NO'

n = int(raw_input())
for _ in xrange(n):
    print hackerrank(raw_input())

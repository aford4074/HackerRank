'''
ACM IPC Team

www.hackerrank.com/challenges/acm-icpc-team

python 2.7

Sample Input

4 5
10101
11100
11010
00101

Sample Output

5
2
'''

from itertools import combinations

n, m = map(int, raw_input().split(' '))
people = [raw_input()[:m] for _ in xrange(n)]

max_topics = 0
max_teams = 0

for p1, p2 in combinations(people, 2):
    topics = bin(int(p1, 2) | int(p2, 2)).count('1')

    if topics > max_topics:
        max_topics = topics
        max_teams = 0

    if topics == max_topics:
        max_teams += 1

print max_topics
print max_teams

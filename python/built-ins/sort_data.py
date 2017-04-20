'''
Sort Data

Sample Input

5 3
10 2 5
7 1 0
9 9 9
1 23 12
6 5 9
1

Sample Output

7 1 0
10 2 5
6 5 9
9 9 9
1 23 12
'''

n, m = map(int, input().split())

table = []

for _ in range(n):
        table.append([val for val in map(int, input().split(' '))])

k = int(input())

for row in sorted(table, key = lambda l: l[k]):
    print(' '.join(map(str, row)))

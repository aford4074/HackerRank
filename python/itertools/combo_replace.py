from itertools import combinations_with_replacement

S, n = input().split(' ')

for s in combinations_with_replacement(sorted(S), int(n)):
    print(''.join(s))

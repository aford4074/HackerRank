from collections import defaultdict

n, m = map(int, input().split(' '))

words = defaultdict(list)

for i, word in [(i, input()) for i in range(1, n + 1)]:
    words[word].append(i)

for word in [input() for _ in range(m)]:
    if word in words:
        print(' '.join(map(str, words[word])))
    else:
        print('-1')

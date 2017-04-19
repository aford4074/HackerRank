from collections import defaultdict

n, m = map(int, input().split(' '))

a_words = defaultdict(list)

for i in range(1, n + 1):
    word = input()

    a_words[word].append(i)

for j in range(m):
    word = input()

    indexes = a_words[word]

    if not len(indexes):
        print('-1')
    else:
        print(' '.join(map(str, indexes)))

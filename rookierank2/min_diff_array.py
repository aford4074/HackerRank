
def hackerrank(a):
    a.sort()

    min_diff = float('inf')

    for i, x in enumerate(a[:-1]):
        if x == a[i+1]:
            return 0

        if abs(x - a[i+1]) < min_diff:
            min_diff = abs(x - a[i+1])

    return min_diff

n = int(raw_input())
a = map(int, raw_input().split(' ')[:n])

print hackerrank(a)

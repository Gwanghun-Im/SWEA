n = int(input())

for i in range(n):
    x, y = input().split()
    x = [int(i) for i in x]
    y = int(y)

    for i in range(y):
        if max(x) != x[0]:
            pass
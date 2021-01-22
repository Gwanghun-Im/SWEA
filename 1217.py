# 1217. [S/W 문제해결 기본] 4일차 - 거듭 제곱

def power(x, y):
    if y == 1:
        return x
    else :
        return x * power(x, y-1)

for _ in range(10):
    i = int(input())
    n, m = map(int, input().split())
    print(f'#{i} {power(n, m)}')

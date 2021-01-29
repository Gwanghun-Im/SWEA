# 1215. 장애물 경주 난이도

T = int(input())
for t in range(T):
    n = int(input())
    height = list(map(int, input().split()))

    d = []
    for i in range(n-1):
        d += [height[i+1] - height[i]]

    d.sort()
    if d[0] > 0:
        print(f'#{t+1} {d[-1]} {0}')        
    elif d[-1] < 0:
        print(f'#{t+1} {0} {-d[0]}')
    else :
        print(f'#{t+1} {d[-1]} {-d[0]}')
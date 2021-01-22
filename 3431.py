# 3431. 준환이의 운동관리

n = int(input())

for i in range(1, n+1):
    a, b, c = map(int, input().split())
    
    if c > b :
        print(f'#{i} -1')
    elif c < a:
        print(f'#{i} {a-c}')
    else :
        print(f'#{i} 0')
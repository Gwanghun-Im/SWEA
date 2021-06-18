from itertools import combinations
import heapq
import copy

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

for n in range(int(input())):
    N, M = map(int, input().split())
    dansik = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    is_human = []
    h = []
    for i in range(N):
        for j in range(M):
            if dansik[i][j] == 0:
                is_human.append([i, j])
            elif dansik[i][j] == 2:
                heapq.heappush(h, [i,j])

    for a, b, c in list(combinations(is_human, 3)):
        temp = copy.deepcopy(dansik)
        temp[a[0]][a[1]] = 1
        temp[b[0]][b[1]] = 1
        temp[c[0]][c[1]] = 1
        temp_ans = 0
        temp_h = h[:]
        while temp_h:
            y, x = heapq.heappop(temp_h)
            for d in range(4):
                my = y + dy[d]
                mx = x + dx[d]
                if 0<=my<N and 0<=mx<M and temp[my][mx]==0:
                    temp[my][mx] = 2
                    heapq.heappush(temp_h, [my, mx])
        for i in range(N):
            for j in range(M):
                if temp[i][j]==0:
                    temp_ans += 1
        if ans < temp_ans:
            ans = temp_ans
    print(f'#{n+1} {ans}')
    

            


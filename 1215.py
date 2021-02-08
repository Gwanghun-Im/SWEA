# 1215. [S/W 문제해결 기본] 3일차 - 회문1

for t in range(10):
    word = []
    cnt = 0

    n = int(input())
    for _ in range(8):
        word.append(input())
    word_T = [list(x) for x in zip(*word)]

    for i in range(8):
        for j in range(8):

            temp = word[i][j:j+n]
            if len(temp) < n:
                continue

            if temp == temp[::-1]:
                cnt += 1

            temp_ = word_T[i][j:j+n]
            if temp_ == temp_[::-1]:
                cnt += 1

    print(f'#{t+1} {cnt}')
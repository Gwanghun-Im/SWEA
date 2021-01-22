#1230. [S/W 문제해결 기본] 8일차 - 암호문3

for temp in range(10):
    N = int(input())
    og = list(map(int, input().split()))
    n_command = int(input())
    command = list(input().split())

    for i in range(n_command):

        if command[0] == 'I':
            x = int(command[1])
            y = int(command[2])
            for j in range(y):
                og.insert(x+j, int(command[3+j]))
            del command[0:y+3]

        elif command[0] == 'D':
            x = int(command[1])
            y = int(command[2])
            del og[x+1 : x+y+1]
            del command[0:3]

        elif command[0] == 'A':
            y = int(command[1])
            for j in range(y):
                og.append(int(command[2+j]))
            del command[0:y+2]

    print(f'#{temp+1} ',end='')
    for i in range(10) : 
        print(f'{og[i]} ',end='')

    print()




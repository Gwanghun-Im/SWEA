n = int(input())

def solve(a, b):
    if len(b) >= len(a):
        for i in range(len(a)):
            if b[i] != a[i]:
                return 'Y'
        if b[i+1] == b[-1] == 0:
            return 'N'

    if len(a) > len(b):
        if len(a) == 10:
            if len(b) >= 2:
                return 'Y'
            if len(b) == 1:
                if b[0] == (a[0]+1):
                    return 'N'
        return 'Y'


for tc in range(1, n+1):
    p = input()
    q = input()

    p_li = []
    q_li = []
    for i in p:
        p_li.append(ord(i)-97)
    for i in q:
        q_li.append(ord(i)-97)
    print('#{} {}'.format(tc, solve(p_li, q_li)))

    

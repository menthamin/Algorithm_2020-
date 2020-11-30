import sys
sys.stdin=open("input.txt", "r")

import time
start = time.time()  # 시작 시간 저장

def DFS(L, P):
    global cnt
    if L == n:
        for idx in range(P):
            print(chr(res[idx]+64), end='')
        print()
        cnt +=1
        return
    else:
        ''' 
        1~26까지 분기
        '''
        for i in range(1, 27):
            if c[L] == i:
                res[P] = i
                DFS(L+1, P+1)
            elif i>=10 and i//10 == c[L] and i%10 == c[L+1]:
                res[P] = i
                DFS(L+2, P+1)

if __name__=="__main__":
    c = list(map(int, input()))
    n = len(c)
    ''' 알파코드 맵 생성 '''
    # alpha_map = dict(zip([str(x) for x in range(1,27)], [chr(x) for x in range(65, 65+27)]))
    c.insert(n, -1)
    cnt = 0
    res = [0]*(n+3)
    DFS(0, 0)
    print(cnt)


print("time :", time.time() - start) 
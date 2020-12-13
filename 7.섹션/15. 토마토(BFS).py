import sys
from collections import deque
import time
sys.stdin=open("input.txt", "r")
""" 4방향 """
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

st_time = time.time()

""" chk 함수 토마토가 모두 익었으면 True, 아니면 False 반환 """
def chk(input_list):
    for row in input_list:
        if 0 in row:
            return False
    else:
        return True


if __name__=="__main__":
    """ input 및 초기화 """
    M, N = map(int, input().split())
    T = [list(map(int,input().split())) for _ in range(N)]
    
    """ 최초 익은 토마토(1) 좌표 q에 넣기"""
    q = deque()
    for i in range(N):
        for j in range(M):
            if T[i][j]==1:
                q.append((i, j))
    cnt = 0
    s_len = len(q)
    n_len = 0

# 고민, 몇번째인지 어떻게 확인할 수 있을까? 

    while q:
        """ 모두 익은 경우 break """
        if chk(T):
            if n_len != 0:
                cnt+=1
            break
        else:
            x, y = q.popleft()
            s_len -=1

            for idx in range(4):
                xx = x+dx[idx]
                yy = y+dy[idx]
                if 0<=xx<N and 0<=yy<M and T[xx][yy]==0:
                    n_len +=1
                    q.append((xx, yy))
                    T[xx][yy] = 1
            
            if s_len == 0:
                cnt +=1
                s_len = n_len
                n_len = 0
                # print(cnt)
                # for row in T:
                #     print(row)
    """ 결과 출력 
        모두 익은 경우와 모두 익지 못하는 경우 
    """
    if chk(T):
        print(cnt)
    else:
        print(-1)

    print(time.time()-st_time)
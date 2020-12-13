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
    """ input 및 초기화 
        T = 토마토
        dis = BFS 깊이 측정용
    """
    M, N = map(int, input().split())
    T = [list(map(int,input().split())) for _ in range(N)]
    dis = [[0]*M for _ in range(N)]
    
    """ 익어있는 토마토(1) 좌표 q에 넣기"""
    q = deque()
    for i in range(N):
        for j in range(M):
            if T[i][j]==1:
                q.append((i, j))

    while q:
        """ 모두 익은 경우 break """
        if chk(T):
            break
        else:
            x, y = q.popleft()
            for idx in range(4):
                xx = x+dx[idx]
                yy = y+dy[idx]
                if 0<=xx<N and 0<=yy<M and T[xx][yy]==0:
                    q.append((xx, yy))
                    T[xx][yy] = 1
                    dis[xx][yy] = dis[x][y]+1
    """ 결과 출력 
        모두 익은 경우와 모두 익지 못하는 경우 
    """

    if chk(T):
        print(max(map(max, dis)))
    else:
        print(-1)

    print(time.time()-st_time)

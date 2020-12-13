import sys
import copy
import time

sys.stdin=open("input.txt", "r")
""" 4방향 """
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

""" 시간 체크 """
st_time = time.time()


if __name__=="__main__":
    """ input 및 초기화 """
    N = int(input())
    M = [list(map(int,input().split())) for _ in range(N)]
    res = []
    for h in range(1, 101):
        """ 높이 1~100까지 확인, 각 경우들 확인을 위해
            배열 deepcopy 및 cnt 초기화 
        """
        mm = copy.deepcopy(M)
        cnt = 0
        """ BFS """
        for i in range(N):
            for j in range(N):
                if mm[i][j] > h:
                    cnt+=1
                    q = []
                    q.append((i,j))
                    while q:
                        x, y = q.pop(0)
                        for idx in range(4):
                            xx = x+dx[idx]
                            yy = y+dy[idx]
                            if 0<=xx<N and 0<=yy<N and mm[xx][yy]>h:
                                mm[xx][yy]=0
                                q.append((xx,yy))
        res.append(cnt)
    print(max(res))
    print(time.time()-st_time)
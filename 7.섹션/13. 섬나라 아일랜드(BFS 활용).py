import sys
sys.stdin=open("input.txt", "r")
""" 시작점 초기화 및 이동방향(8개) 설정 
    12시부터 시계방향
"""
dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

if __name__=="__main__":
    """ input 및 초기화 """
    N = int(input())
    M = [list(map(int,input().split())) for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if M[i][j] == 1:
                cnt +=1
                q = []
                q.append((i,j))
                while q:
                    x, y = q.pop(0)
                    for idx in range(8):
                        xx = x+dx[idx]
                        yy = y+dy[idx]
                        if 0<=xx<N and 0<=yy<N and M[xx][yy]==1:
                            M[xx][yy]=0
                            q.append((xx,yy))
    print(cnt)

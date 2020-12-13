import sys
sys.stdin=open("input.txt", "r")
""" 시작점 초기화 및 이동방향(12시, 3시, 6시, 9시) 설정 """
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]


def DFS(x, y):
    global cnt
    cnt+=1
    M[x][y] = 0
    for idx in range(4):
        xx = x+dx[idx]
        yy = y+dy[idx]
        if 0<=xx<N and 0<=yy<N and M[xx][yy]==1:
            DFS(xx, yy)

if __name__=="__main__":
    """ input 및 초기화 """
    N = int(input())
    M = [list(map(int,input())) for _ in range(N)]

    res = []
    for i in range(N):
        for j in range(N):
            if M[i][j] == 1:
                cnt = 0
                DFS(i, j)
                res.append(cnt)       

    print(len(res))
    res.sort()
    for x in res:
        print(x)


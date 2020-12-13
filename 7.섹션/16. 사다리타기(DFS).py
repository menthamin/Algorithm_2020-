import sys
from collections import deque
sys.stdin=open("input.txt", "r")
""" 3방향 좌, 우, 상"""
dx = [0, 0, -1]
dy = [-1, 1, 0]

def DFS(x, y):
    if x == 0:
        return print(y)
    for idx in range(3):
        xx = x+dx[idx]
        yy = y+dy[idx]
        if 0<=xx<10 and 0<=yy<10 and T[xx][yy] == 1:
            T[xx][yy] = 0
            DFS(xx, yy)
            break

if __name__=="__main__":
    T = [list(map(int,input().split())) for _ in range(10)]
    
    ''' 시작지점 찾기 '''
    x = None
    y = None
    for i in range(10):
        for j in range(10):
            if T[i][j] == 2:
                x, y = i, j

    DFS(x, y)
    

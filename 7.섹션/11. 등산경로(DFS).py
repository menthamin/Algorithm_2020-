import sys
sys.stdin=open("input.txt", "r")

def DFS(p):
    global cnt
    if p[0] == dst_p[0] and p[1] == dst_p[1]:
        cnt +=1
        return  
    for idx in range(4):
        x = p[0]+dx[idx]
        y = p[1]+dy[idx]
        ''' 이동 가능 조건 3가지 충족 확인 : 1. 미로범위안, 2. 길, 3. 안간길 '''
        if 0<=x<N and 0<=y<N and M[x][y] > M[p[0]][p[1]] and chk[x][y] == 0:
            # 들른길로 체크
            chk[x][y] = 1
            DFS((x, y))
            # 체크 해제
            chk[x][y] = 0

if __name__=="__main__":
    """ input 및 초기화 """
    N = int(input())
    M = [list(map(int, input().split())) for _ in range(N)]
    chk = [[0]*N for _ in range(N)]
    """ 시작점 초기화 및 이동방향(12시, 3시, 6시, 9시) 설정 """
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    cnt = 0 
    src_v = (2147300000, 0, 0)
    dst_v = (-2147300000, 0, 0)
    for x in range(N):
        for y in range(N):
            if src_v[0] > M[x][y]:
                src_v = (M[x][y], x, y)

            if dst_v[0] < M[x][y]:
                dst_v = (M[x][y], x, y)
    src_p = src_v[1:]
    dst_p = dst_v[1:]
    """ 시작 """ 
    chk[src_p[0]][src_p[1]] = 1
    
    DFS(src_p)
    print(cnt)


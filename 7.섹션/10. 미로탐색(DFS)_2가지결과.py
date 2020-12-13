import sys
sys.stdin=open("input.txt", "r")

# 2가지 결과로 풀어본다
# 1. 방법의 수만
# 2. 방법의 수 + 몇번에 도착했는지 까지

def DFS(p, chk, L):
    global cnt
    if p[0] == 6 and p[1] == 6:
        # print(L)
        cnt +=1  
    for idx in range(4):
        x = p[0]+dx[idx]
        y = p[1]+dy[idx]
        ''' 이동 가능 조건 3가지 충족 확인 : 1. 미로범위안, 2. 길, 3. 안간길 '''
        if 0<=x<=6 and 0<=y<=6 and M[x][y] == 0 and chk[x][y] == -1:
            # 들른길로 체크
            chk[x][y] = 0
            DFS([x, y], chk, L+1)
            # 체크 해제
            chk[x][y] = -1

if __name__=="__main__":
    ''' input 및 초기화 '''
    M = [list(map(int, input().split())) for _ in range(7)]
    chk = [[-1]*7 for _ in range(7)]
    ''' 시작점 초기화 및 이동방향(12시, 3시, 6시, 9시) '''
    sp = [0, 0]
    chk[0][0] = 0 # 풀어주기 필요
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]

    cnt = 0 
    DFS(sp, chk, 0)
    print(cnt)
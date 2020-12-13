import sys
sys.stdin=open("input.txt", "r")

if __name__=="__main__":
    ''' input 및 초기화 '''
    M = [list(map(int, input().split())) for _ in range(7)]
    chk = [[-1]*7 for _ in range(7)]
    ''' 시작점 초기화 및 이동방향(12시, 3시, 6시, 9시) '''
    sp = [0, 0]
    chk[0][0] = 0
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    ''' BFS '''
    q = []
    q.append(sp)
    
    # 성공여부 체크용
    chk_com = 0
    while q:
        tmp = q.pop(0)
        for idx in range(4):
            x = tmp[0]+dx[idx]
            y = tmp[1]+dy[idx]
            if 0<=x<=6 and 0<=y<=6 and chk[x][y] == -1 and M[x][y] == 0:
                chk[x][y] = chk[tmp[0]][tmp[1]]+1
                q.append([x,y])
    # 불가능시 -1 반환
    if chk[6][6] == -1:
        print(-1)
    else:
        print(chk[6][6])
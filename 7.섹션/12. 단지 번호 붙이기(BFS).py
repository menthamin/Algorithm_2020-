import sys
sys.stdin=open("input.txt", "r")

if __name__=="__main__":
    """ input 및 초기화 """
    N = int(input())
    M = [list(map(int,input())) for _ in range(N)]
    """ 시작점 초기화 및 이동방향(12시, 3시, 6시, 9시) 설정 """
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]

    cnt_list = []
    for i in range(N):
        for j in range(N):
            q = []
            if M[i][j] == 1:
                M[i][j] = 0
                q.append((i, j))
                cnt = 1
                ''' 조건들 
                    Index범위를 넘지 않을 것
                    1일 것
                '''
                while q:
                    x, y = q.pop()
                    for idx in range(4):
                        xx = x+dx[idx]
                        yy = y+dy[idx]
                        if 0<=xx<N and 0<=yy<N and M[xx][yy]==1:
                            M[xx][yy] = 0
                            q.append((xx,yy))
                            cnt+=1
                cnt_list.append(cnt)                 

    print(len(cnt_list))
    cnt_list.sort()
    for x in cnt_list:
        print(x)


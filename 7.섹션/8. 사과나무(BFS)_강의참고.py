import sys
sys.stdin=open("input.txt", "r")

if __name__=="__main__":
    N = int(input())
    ''' 사과 농장 값 받기 '''
    N_matrix = []
    for _ in range(N):
        tmp = list(map(int, input().split()))
        N_matrix.append(tmp)

    ''' 사과나무 체크 matrix '''
    chk_matrix = [[0]*N for _ in range(N)]


    ''' 시작점 및 이동방향(12시, 3시, 6시, 9시) '''
    st_point = [N//2, N//2]
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    
    ''' 초기화 '''
    tot = 0
    q = []
    q.append(st_point)
    tot += N_matrix[st_point[0]][st_point[1]]
    chk_matrix[st_point[0]][st_point[1]] = 1
    L = 0
    ''' 전체 ''' 
    ''' 멈추는걸 어떻게 구현할지 ? '''
    while q:
        if L == N//2:
            break
        size = len(q)
        for i in range(size):
            point = q.pop(0)
            for idx in range(4):
                n_point = [point[0]+dx[idx], point[1]+dy[idx]]
                # if n_point[0] >=0 and n_point[1] >=0 and n_point[0] < N and n_point[1] < N:
                if chk_matrix[n_point[0]][n_point[1]] == 0:
                    tot += N_matrix[n_point[0]][n_point[1]]
                    chk_matrix[n_point[0]][n_point[1]] = 1
                    q.append(n_point)
        L+=1

    print(tot)
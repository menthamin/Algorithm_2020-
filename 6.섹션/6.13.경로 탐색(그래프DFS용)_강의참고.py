import sys
# import itertools as it
sys.stdin=open("input.txt", "r")

def DFS(node):
    global cnt
    if node == (N-1):
        cnt+=1
        for x in path:
            print(x, end=' ')
        print()
        return
    if cnt >= N:
        return
    
    # 다른 종료조건은 안 넣어도 된다는게 신기
    for idx in range(N):
        # 2가지 조건이 맞아야한다. matrix에서 1 and 안갔던길
        if path_matrix[node][idx]==1 and chk[idx]==0:
            chk[idx] = 1
            path.append(idx+1)
            DFS(idx)
            path.pop()
            chk[idx] = 0

if __name__=="__main__":
    N, M = map(int, input().split())
    ''' 가중치 매트릭스 초기화 '''
    path_matrix = [[0 for _ in range(N)] for _ in range(N)]

    for _ in range(M):
        i, j = map(int, input().split())
        path_matrix[i-1][j-1] = 1
    chk = [0]*N
    chk[0] = 1

    cnt = 0
    path = []
    path.append(1)

    DFS(0)
    print(cnt)
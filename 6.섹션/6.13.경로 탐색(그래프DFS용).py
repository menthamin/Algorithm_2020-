import sys
# import itertools as it
sys.stdin=open("input.txt", "r")

def DFS(node, chk, cnt):
    global res
    if node == (N-1):
        res+=1
        # for idx, value in enumerate(chk):
        #     if value==1:
        #         print(idx+1, end=" ")
        # print()
        return
    if cnt >= N:
        return
    
    for idx in range(N):
        # 2가지 조건이 맞아야한다. matrix에서 1 and 안갔던길
        if path_matrix[node][idx]==1 and chk[idx]==0:
            chk[idx] = 1
            DFS(idx, chk, cnt+1)
            chk[idx] = 0

if __name__=="__main__":
    N, M = map(int, input().split())
    ''' 가중치 매트릭스 초기화 '''
    path_matrix = [[0 for _ in range(N)] for _ in range(N)]

    for _ in range(M):
        i, j = map(int, input().split())
        path_matrix[i-1][j-1] = 1
    # for i in range(N):
    #     path_matrix[i][i] = 1
    # print(path_matrix[0])
    chk = [0]*N
    chk[0] = 1
    res = 0
    # for row in path_matrix:
    #     print(row)
    DFS(0, chk, 0)
    print(res)
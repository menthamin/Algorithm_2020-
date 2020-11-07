import sys
sys.stdin=open("input.txt", "r")

def DFS(L, res):
    # 종료조건
    global cnt
    if L==M:
        cnt+=1    
        for i in range(M):
            print(res[i], end=" ")
        print()
        return
    else:
        # 트리전개 3 방향으로
        for i in range(1, N+1):
            res[L]=i
            DFS(L+1, res)

if __name__=="__main__":
    N, M=map(int, input().split())
    res=[0]*M
    cnt = 0
    DFS(0, res)
    print(cnt)
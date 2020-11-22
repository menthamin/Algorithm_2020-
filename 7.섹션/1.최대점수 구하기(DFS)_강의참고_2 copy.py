import sys
sys.stdin=open("input.txt", "r")


def DFS(L, sum, T):
    global max_value
    if T > M:
        return
        
    if L == N:
        if sum > max_value:
            max_value = sum
        return
    else:
        DFS(L+1, sum+exam[L][0], T+exam[L][1])
        DFS(L+1, sum, T)

if __name__=="__main__":
    N, M = map(int, input().split())
    # (점수,시간)
    exam = [list(map(int, input().split())) for _ in range(N)] 
    max_value = -21470000
    DFS(0, 0, 0)
    print(max_value)
import sys
sys.stdin=open("input.txt", "r")


# 왜 시간 초과가 나올까? 트리 전체를 도는게 맞지 않은지.
def DFS(L, sum, T):
    global max_value
    # 종료조건, 끝까지 간 경우
    if L == N:
        if sum > max_value:
            max_value = sum
        return
    else:
        # 작은 경우에는 선택/미선택 두개 모두 가능, 큰경우에는 선택하지 않는 경우만 전개
        # T <= M
        if (T+exam[L][1]) <= M:
            # 푼다. 안푼다 모두
            DFS(L+1, sum+exam[L][0], T+exam[L][1])
            DFS(L+1, sum, T)
        else:
            DFS(L+1, sum, T)

if __name__=="__main__":
    N, M = map(int, input().split())
    # (점수,시간)
    exam = [list(map(int, input().split())) for _ in range(N)] 
    max_value = -21470000
    DFS(0, 0, 0)
    print(max_value)
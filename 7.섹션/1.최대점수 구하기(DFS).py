import sys
sys.stdin=open("input.txt", "r")


# 왜 시간 초과가 나올까? 트리 전체를 도는게 맞지 않은지. 문제 개수만큼 계속 반복해서.. 오래걸린다.
def DFS(L, T, sum):
    global max_value
    # 종료 조건
    if L >= N or T == M:
        if sum > max_value:
            max_value = sum
        return
    # DFS
    for idx, i in enumerate(chk):
        # 풀지 않은 경우
        if i == 0:
            chk[idx] = 1
            # 시간 초과 X
            if (T+exam[idx][1]) <= M:
                DFS(L+1, T+exam[idx][1], sum+exam[idx][0])
                chk[idx] = 0
            # 시간 초과
            else:
                if sum > max_value:
                    max_value = sum
                chk[idx] = 0
                return

if __name__=="__main__":
    N, M = map(int, input().split())
    # (점수,시간)
    exam = [list(map(int, input().split())) for _ in range(N)] 
    chk = [0] * N
    max_value = 0
    DFS(0, 0, 0)
    print(max_value)
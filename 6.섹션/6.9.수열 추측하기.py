import sys
sys.stdin=open("input.txt", "r")


def com_sum(L, init_list, next_list):
    if L == N-1:
        if sum(next_list) == F:
            for i in init_list:
                print(i, end=' ')
            sys.exit()
        return True
    temp = []
    for idx in range(len(next_list)-1):
        temp.append(next_list[idx] + next_list[idx+1])
        com_sum(L+1, init_list, temp)


def DFS(L):
    if L == N:
        combi = []
        for i in range(N):
            combi.append(res[i])
        com_sum(0, combi, combi)
        return
    # 트리 분지
    for i in range(N):
        if chk[i]==0:
            # res[L] = <- 이게 새로운 리스트를 생성하는것으로 인식되는 것이 아니다
            res[L] = i+1
            chk[i] = 1 # 다음번에 이녀석은 못쓰도록 체크하고 재귀함수로 보낸다.
            DFS(L+1)
            # DFS가 종료되고(return) 다음번에 쓸 수 있도록 0으로 풀어준다
            chk[i] = 0

if __name__=="__main__":
    N, F = map(int, input().split())
    chk = [0]*N
    res = [0]*N
    DFS(0)
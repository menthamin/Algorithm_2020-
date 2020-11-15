import sys
sys.stdin=open("input.txt", "r")
''' 제일 앞 숫자를 재활용 못하네 '''
def DFS(L, S):
    global cnt
    if L == K:
        if sum(res) % M == 0:
            cnt+=1
            # print(res)
        return
    else:
        for idx in range(S,N):
            res[L] = N_list[idx]
            DFS(L+1, idx+1)


if __name__=="__main__":
    ''' Input N, N_list, M '''
    N, K = map(int, input().split())
    N_list = list(map(int, input().split()))
    M = int(input())
    # print(N, K, N_list, K)
    res = [0]*K
    cnt = 0
    DFS(0, 0)
    print(cnt)
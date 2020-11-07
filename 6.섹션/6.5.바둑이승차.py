import sys
sys.stdin=open("input.txt", "r")

def DFS(x, sum, tsum):

    # 종료조건 0 (앞으로 남은것들을 다 더해도 max값이 안되는 경우)
    if sum+(tot-tsum) < max(sum_list):
        return
    # 종료조건 1
    if sum > C:
        # 여기 위쪽으로는 모두 확인할 필요가 없어진다
        return
    # 종료조건 2
    if x==N:
        sum_list.append(sum)
        return
    else:
        # 이진트리 전개
        DFS(x+1, sum+N_list[x], sum+N_list[x])
        DFS(x+1, sum, sum+N_list[x])

if __name__=="__main__":
    C, N=map(int, input().split())
    N_list=[int(input()) for _ in range(N)]
    tot=sum(N_list)
    sum_list=[0]
    DFS(0, 0, 0)
    print(max(sum_list))
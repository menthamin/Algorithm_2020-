import sys
sys.stdin=open("input.txt", "r")

def DFS(L, sum):
    global res
    # Cut Edge
    if res <= L:
        return 
    if sum > T_num:
        return
    elif sum == T_num:
        if res > L:
            res = L
        return 
    else:
        # 트리전개
        for idx in range(N):
            # 깊이 우선 탐색이여서..
            DFS(L+1, sum+N_list[idx])

if __name__=="__main__":
    N = int(input())
    N_list = list(map(int, input().split()))
    T_num = int(input())
    res = 2147000000
    N_list.sort(reverse=True)
    DFS(0, 0)
    print(res)
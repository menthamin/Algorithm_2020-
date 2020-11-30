import sys
sys.stdin=open("input.txt", "r")

''' +, = , - 3개 가지로 분기 '''
def DFS(L, sum):
    if L == N:
        if sum >= 1 :
            res.add(sum)
        return
    else:
        DFS(L+1, sum+N_list[L])
        DFS(L+1, sum)
        DFS(L+1, sum-N_list[L])

if __name__=="__main__":
    N = int(input())
    N_list = list(map(int, input().split()))
    s = sum(N_list)
    res = set()
    DFS(0, 0)
    print(s-len(res))
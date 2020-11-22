import sys
sys.stdin=open("input.txt", "r")


def DFS(L, sum):
    global res
    if L > N:
        return
    if L == N:
        if sum > res:
            res = sum
        return
    else:
        DFS(L+st[L], sum+sp[L])
        DFS(L+1, sum)

if __name__=="__main__":
    N = int(input())
    st = []
    sp = []
    for _ in range(N):
        a, b = map(int, input().split())
        st.append(a)
        sp.append(b)
    res = -21470000
    DFS(0, 0)
    print(res)
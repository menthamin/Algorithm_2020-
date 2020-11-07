import sys
sys.stdin=open("input.txt", "r")

def DFS(x):
    if x==n+1:
        for i in range(1, n+1):
            if ch[i]==1:
                print(i, end=' ')
        print()
    else:
        # 사용하는 상태 트리
        ch[x]=1
        DFS(x+1)
        # 사용하지않는 상태 트리
        ch[x]=0
        DFS(x+1)

if __name__=="__main__":
    n=int(input())
    # 상태체크용
    ch=[0]*(n+1)
    DFS(1)
import sys
sys.stdin=open("input.txt", "r")

def DFS(x):
    if x==N:
        sub1 = 0
        sub2 = 0
        for i in range(N):
            if ch[i]==1:
                sub1+=N_list[i]
            else:
                sub2+=N_list[i]
        if sub1==sub2:
            global cnt
            cnt+=1

    else:
        # 이진트리 전개
        ch[x]=1
        DFS(x+1)
        ch[x]=0
        DFS(x+1)

if __name__=="__main__":
    N=int(input())
    N_list=list(map(int, input().split()))
    # 상태체크용
    ch=[0]*N
    cnt=0
    DFS(0)
    if cnt>=1:
        print("YES")
    else:
        print("NO")
import sys
sys.stdin=open("input.txt", "r")
''' 제일 앞 숫자를 재활용 못하네 '''
def DFS(L, S):
    global cnt
    if L == M:
        for i in res:
            print(i, end=" ")
        print()
        cnt+=1
        return

    if S > N:
        return 

    for i in range(S,N+1):
        res[L] = i
        DFS(L+1, i+1)


if __name__=="__main__":
    ''' Input N, M '''
    N, M = map(int, input().split())
    # 출력을 i+1로
    res = [0]*M
    cnt=0 
    DFS(0, 1)
    print(cnt)
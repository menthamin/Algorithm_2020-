import sys
sys.stdin=open("input.txt", "r")

def DFS(L):
    global cnt
    if L == M:
        cnt +=1
        for i in range(M):
            print(res[i], end = ' ')
        print()
        return
    # 트리 분지
    for i in range(N):
        if chk[i]==0:
            # res[L] = <- 이게 새로운 리스트를 생성하는것으로 인식되는 것이 아니다
            res[L] = i+1 9
            chk[i] = 1 # 다음번에 이녀석은 못쓰도록 체크하고 재귀함수로 보낸다.
            DFS(L+1)
            # DFS가 종료되고(return) 다음번에 쓸 수 있도록 0으로 풀어준다
            chk[i] = 0

if __name__=="__main__":
    N, M = map(int, input().split())
    cnt = 0
    chk = [0]*N
    res = [0]*M
    DFS(0)
    print(cnt)
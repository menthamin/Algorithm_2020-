import sys
sys.stdin=open("input.txt", "r")

''' +, = , - 3개 가지로 분기 '''
def DFS(L, sum):
    if L == N:
        if sum >= 1 :
            chk[sum] = 0
        return
    else:
        DFS(L+1, sum+N_list[L])
        DFS(L+1, sum)
        DFS(L+1, sum-N_list[L])

if __name__=="__main__":
    N = int(input())
    N_list = list(map(int, input().split()))
    # 확인용 변수 초기화
    chk = [1] * (sum(N_list)+1)
    chk[0] = 0 
    DFS(0, 0)
    print(sum(chk))

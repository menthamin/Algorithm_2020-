import sys
sys.stdin=open("input.txt", "r")

''' 전체 경우의수로 접근 = 실패 '''
def DFS(L, sum):
    global cnt
    if sum > T:
        return
    if L == len(K_list):
        if sum == T:
            cnt += 1
        return
    else:
        DFS(L+1, sum+K_list[L])
        DFS(L+1, sum)

if __name__=="__main__":
    T = int(input())
    K = int(input())
    K_info = [list(map(int, input().split())) for _ in range(K)]
    K_list = []
    for value, num in K_info:
        K_list += [value]*num
    cnt = 0
    DFS(0, 0)
    print(cnt)
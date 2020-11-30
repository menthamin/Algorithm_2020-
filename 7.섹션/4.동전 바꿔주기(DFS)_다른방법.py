import sys
sys.stdin=open("input.txt", "r")

''' 다른방법으로 접근'''
def DFS(L, sum):
    global cnt
    if sum > T:
        return
    if L == K:
        if sum == T:
            cnt += 1
        return
    else:
        ''' 동전별 경우의 수 분기 '''
        for idx in range(len(K_list[L])):
            DFS(L+1, sum+K_list[L][idx])

if __name__=="__main__":
    T = int(input())
    K = int(input())
    K_info = [list(map(int, input().split())) for _ in range(K)]
    K_list = []
    ''' 동전 경우의 수 초기화 '''
    for value, num in K_info:
        tmp = []
        for i in range(num+1):
            tmp.append(value*i)
        K_list.append(tmp)

    cnt = 0
    DFS(0, 0)
    print(cnt)
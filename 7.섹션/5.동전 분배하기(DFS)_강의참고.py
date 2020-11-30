import sys
sys.stdin=open("input.txt", "r")

def DFS(L):
    global res
    if L == N:
        diff = max(money) - min(money)
        if diff < res:
            tmp = set()
            for x in money:
                tmp.add(x)
            if len(tmp) == 3:
                res = diff
        return
    else:
        ''' 
        3가지 경우로 분기
        분기 후에는 더해줬던 값을 빼줘야함 
        '''
        for idx in range(3):
            money[idx] += N_list[L]
            DFS(L+1)
            money[idx] -= N_list[L]

if __name__=="__main__":
    N = int(input())
    N_list = [int(input()) for _ in range(N)]
    money = [0]*3
    res = 214700000
    DFS(0)
    print(res)
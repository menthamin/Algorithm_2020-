import sys
sys.stdin=open("input.txt", "r")

def DFS(L, V):
    global res
    if L == N:
        ''' 중복확인 : V[0] != V[1] != V[2] 이 규칙은 유효하지 않음 '''
        ''' 유효한 중복확인 '''
        if V[0] != V[1] and V[0] != V[2] and V[1] != V[2]:
            diff = max(V) - min(V)
            if diff < res:
                res = diff
        return
    else:
        ''' 3가지 경우로 분기 '''
        ''' 각 A,B,C에게 주는 경우'''
        DFS(L+1, [V[0]+N_list[L], V[1], V[2]])
        DFS(L+1, [V[0], V[1]+N_list[L], V[2]])
        DFS(L+1, [V[0], V[1], V[2]+N_list[L]])

if __name__=="__main__":
    N = int(input())
    N_list = [int(input()) for _ in range(N)]
    res = 213700000
    DFS(0, [0,0,0])
    print(res)
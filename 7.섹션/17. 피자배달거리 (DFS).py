import sys
sys.stdin=open("input.txt", "r")

# 피자집 선택 N개중 M개 선택 (조합알고리즘)
def DFS(L, s):
    global res
    if L == M:
        disT = 0
        # 집별로 가장 가까운 피자집 구하기
        for x, y in h:
            dis_min = 21470000
            for idx, value in enumerate(chk):
                if value == 1:
                    px, py = p[idx]
                    dis = abs(x-px)+abs(y-py)
                    if dis < dis_min:
                        dis_min = dis
            disT += dis_min
        if disT < res:
            res = disT
    for idx in range(s, len(p)):
        chk[idx] = 1
        DFS(L+1, idx+1)
        chk[idx] = 0
 
if __name__=="__main__":
    N, M = map(int, input().split())
    T = [list(map(int,input().split())) for _ in range(N)]
    
    ''' 집, 피자집 좌표 저장 '''
    h = []
    p = []
    for i in range(N):
        for j in range(N):
            if T[i][j] == 1:
                h.append((i,j))
            elif T[i][j] == 2:
                p.append((i,j))
    chk = [0] * len(p)
    res = 21470000
    DFS(0, 0)
    print(res)

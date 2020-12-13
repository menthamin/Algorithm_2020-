import sys
sys.stdin=open("input.txt", "r")

if __name__=="__main__":
    S, E = map(int, input().split())
    dis = [0]*10001
    chk = [0]*10001
    q = []
    q.append(S)
    chk[S] = 1

    while q:
        now = q.pop(0)
        if now == E:
            break
        for next in(now-1, now+1, now+5):
            if 0<next<=10000 and chk[next]==0:
                q.append(next)
                chk[next] = 1
                dis[next] = dis[now] + 1

print(dis[E])
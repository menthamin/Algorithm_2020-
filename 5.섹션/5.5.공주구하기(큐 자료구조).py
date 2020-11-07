import sys
from collections import deque

sys.stdin=open("input.txt","rt")
# 입력받기
N, M=map(int, input().split())
N_list=[i+1 for i in range(N)]
q=deque(N_list)

while len(q)!=1:
# 다음값을 어떻게 찾아가게 할것인가 (환형 큐)
    for _ in range(M-1):
        cur=q.popleft()
        q.append(cur)
    q.popleft()

print(q[0])
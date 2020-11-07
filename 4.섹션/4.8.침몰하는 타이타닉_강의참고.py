import sys
from collections import deque
sys.stdin=open("input.txt","rt")
# 입력받기
N, M=map(int,input().split())
N_list=list(map(int,input().split()))
N_list.sort()
N_deque=deque(N_list)
# N_deque.sort()

cnt=0
# 제일가벼운사람 + 제일무거운사람 조합을 확인해가며 뺀다.
while N_deque:
    # 한명만 남은경우
    if len(N_deque)==1:
        cnt+=1
        break
    else:
        if N_deque[0]+N_deque[-1]>M:
            N_deque.pop()
            cnt+=1
        else:
            N_deque.popleft()
            N_deque.pop()
            cnt+=1
print(cnt)
## 시간초과

import sys

sys.stdin=open("input.txt","rt")
#입력받기
N, M=map(int, input().split())
N_list=list(map(int, input().split()))

cnt=0
for size in range(1,N):
    idx=0
    # idx=6 일때
    while idx+size<=N:
        # print(idx, end=' ')
        if sum(N_list[idx:idx+size])==M:
            cnt+=1
            # print(N_list[idx:idx+size])
        idx+=1
    # print()
print(cnt) 
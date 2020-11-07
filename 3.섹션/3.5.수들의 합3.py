#시간 초과
import sys

sys.stdin=open("input.txt","rt")
#입력받기
N, M=map(int, input().split())
N_list=list(map(int, input().split()))

cnt=0
for idx in range(N):
    r_idx=idx+1
    while r_idx<=N:
        if sum(N_list[idx:r_idx])==M:
            cnt+=1
        elif sum(N_list[idx:r_idx])>M:
            break
        r_idx+=1
print(cnt) 
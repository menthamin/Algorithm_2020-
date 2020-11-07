import sys

sys.stdin=open("input.txt","rt")
#입력받기
N, M=map(int, input().split())
N_list=list(map(int, input().split()))

cnt=0
for size in range(1,N):
    if size>M: # 이조건으로 60%ㅣ
        break
    idx=0
    while idx+size<=N:
        if sum(N_list[idx:idx+size])==M:
            cnt+=1
        idx+=1
print(cnt) 
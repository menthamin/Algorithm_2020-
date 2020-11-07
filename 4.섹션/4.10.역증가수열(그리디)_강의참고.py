import sys
# from collections import deque

sys.stdin=open("input.txt","rt")
# 입력받기
N=int(input())
N_list=list(map(int, input().split()))

# print(N_list)
seq=[0]*N

for num, num_cnt in enumerate(N_list):
    # 만난 0 개수
    cnt=0
    for idx, value in enumerate(seq):
        if cnt==num_cnt and value==0:
            seq[idx]=(num+1)
            breaks
        if value==0:
            cnt+=1
        
for i in seq:
    print(i, end=" ")
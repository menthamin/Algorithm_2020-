import sys

sys.stdin=open("input.txt","rt")
# 입력받기
N=int(input())
N_list=list(map(int,input().split()))
M=int(input())

for _ in range(M):
    max_value=max(N_list)
    min_value=min(N_list)
    N_list[N_list.index(max_value)]-=1
    N_list[N_list.index(min_value)]+=1

print(max(N_list)-min(N_list))
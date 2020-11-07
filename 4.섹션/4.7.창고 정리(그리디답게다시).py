import sys

sys.stdin=open("input.txt","rt")
# 입력받기
N=int(input())
N_list=list(map(int,input().split()))
M=int(input())
N_list.sort()

for _ in range(M):
    N_list[0]+=1
    N_list[-1]-=1
    N_list.sort()

print(N_list[-1]-N_list[0])
import sys

sys.stdin=open("input.txt","rt")
N, M=map(int,input().split())

# 모든 경우의 수를 담는 리스트 만들기
num_list=[0 for _ in range(N+M+1)]

# 경우의 수별 Count
for N in range(1,N+1):
    for M in range(1,M+1):
        num_list[N+M]+=1

# Count중 max값 확인
max_count=max(num_list)

# max 값들의 index 차례대로 출력 
for idx, cnt in enumerate(num_list):
    if cnt==max_count:
        print(idx, end=' ')
import sys
from collections import deque

sys.stdin=open("input.txt","rt")
# 입력받기
N = int(input())
N_list = [input() for _ in range(N)]
T_list = [input() for _ in range(N-1)]

for x in T_list:
    if x in N_list:
        N_list.pop(N_list.index(x))

print(N_list[0])
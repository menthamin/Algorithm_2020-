import sys
from collections import deque

sys.stdin=open("input.txt","rt")
# 입력받기
N = deque(input())
M = deque(input())

for s in N:
    if s in M:
        M.remove(s)

if len(M)==0:
    print("YES")
else:
    print("NO")
import sys
from collections import deque

sys.stdin=open("input.txt","rt")
# 입력받기
N = list(input())
M = list(input())

for s in N:
    if s in M:
        M.pop(M.index(s))

if len(M)==0:
    print("YES")
else:
    print("NO")
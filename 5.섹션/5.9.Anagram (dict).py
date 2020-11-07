import sys
from collections import deque

sys.stdin=open("input.txt","rt")
# 입력받기
n = dict()
m = dict()

for x, y in zip(input(), input()):
    if x in n:
        n[x] += 1
    else:
        n[x] = 1
    if y in m:
        m[y] += 1
    else:
        m[y] = 1

if n == m:
    print("YES")
else:
    print("NO")


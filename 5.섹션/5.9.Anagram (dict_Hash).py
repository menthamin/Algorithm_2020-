import sys
# from collections import deque

sys.stdin=open("input.txt","rt")
# 입력받기
sH = dict()

for x, y in zip(input(), input()):
    sH[x] = sH.get(x,0) + 1
    sH[y] = sH.get(y,0) - 1

for val in sH.values():
    if val!=0:
        print("NO")
        break
else:
    print("YES")

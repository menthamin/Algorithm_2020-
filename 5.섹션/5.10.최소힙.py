import sys
import heapq as hq

sys.stdin=open("input.txt","rt")
# 입력받기
a = []

while True:
    n = int(input())
    if n == -1:
        break
    elif n == 0:
        if len(a)==0:
            print("-1")
        else:
            print(hq.heappop(a)*-1)
    else:
        hq.heappush(a, n*-1)
print(a)

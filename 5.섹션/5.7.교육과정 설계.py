import sys
from collections import deque

sys.stdin=open("input.txt","rt")
# 입력받기
P = input()
N = int(input())
C_list = [input() for _ in range(N)]
for idx, c in enumerate(C_list):
    p_list = list(P)
    for x in c:
        if x in p_list:
            if x == p_list[0]:
                p_list.pop(0)
            else:
                print("#"+str(idx+1)," NO")
                break
    else:
        if p_list:
            print("#"+str(idx+1)," NO")
        else:
            print("#"+str(idx+1)," YES")
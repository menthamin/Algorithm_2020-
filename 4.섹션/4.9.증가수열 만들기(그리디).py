import sys
from collections import deque

sys.stdin=open("input.txt","rt")
# 입력받기
N=int(input())
N_deque=deque(map(int,input().split()))

lt=0
rt=N-1
last=0
res=""
tmp=[]

while lt<=rt:
    if N_deque[lt]>last:
        tmp.append((N_deque[lt], "L"))
    if N_deque[rt]>last:
        tmp.append((N_deque[rt], "R"))
    if len(tmp)==0:
        break
    else:
        tmp.sort(key=lambda x : x[0])
        res+=tmp[0][1]
        last=tmp[0][0]
        if tmp[0][1]=="L":
            lt+=1
        else:
            rt-=1
        tmp=[]

print(len(res))
print(res)
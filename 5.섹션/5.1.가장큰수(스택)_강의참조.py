import sys
# from collections import deque

sys.stdin=open("input.txt","rt")
# 입력받기
N, m=input().split()
N=list(map(int,N))
m=int(m)
stack=[]

for x in N:
    while stack and m>0 and stack[-1]<x:
        stack.pop()
        m-=1
    stack.append(x)

if m!=0:
    stack=stack[:-m]

res="".join(map(str, stack))
print(res)
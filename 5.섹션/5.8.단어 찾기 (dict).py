import sys
# from collections import deque

sys.stdin=open("input.txt","rt")
# 입력받기
N = int(input())
p = dict()

for _ in range(N):
    word = input()
    p[word] = 1

for _ in range(N-1):
    word = input()a
    p[word] = 0

for key , val in p.items():
    if val == 1:
        print(key)
        break
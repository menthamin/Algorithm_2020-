import sys
from collections import deque

sys.stdin=open("input.txt","rt")
# 입력받기
N, M = map(int, input().split())
N_input = map(int, input().split())
N_list = [(i, idx) for idx, i in zip(range(N), N_input)]

cnt = 0

while True:
    num, _ = zip(*N_list)
    max_value = max(num)
    # 제일 큰 값인 경우
    if N_list[0][0] >= max_value:
        cnt += 1
        # idx 값이 M 인 경우, 종료
        if N_list[0][1] == M:
            break
        N_list.pop(0)
    else:
        temp = N_list.pop(0)
        N_list.append(temp)

print(cnt)
import sys
from collections import deque

sys.stdin=open("input.txt","rt")
# 입력받기
N=int(input())
N_deque=deque(map(int,input().split()))


# 초기값 설정
s=[]
d=""
if N_deque[0]>N_deque[-1]:
    s.append(N_deque.pop())
    d+="R"
else:
    s.append(N_deque.popleft())
    d+='L'

while True:
    # 양끝 비교 작은값 부터
    if N_deque[0]>N_deque[-1]:
        if N_deque[-1]>s[-1]:
            s.append(N_deque.pop())
            d+="R"
        elif N_deque[0]>s[-1]:
            s.append(N_deque.popleft())
            d+="L"
        else:
            break        
    else:
        if N_deque[0]>s[-1]:
            s.append(N_deque.popleft())
            d+="L"
        elif N_deque[-1]>s[-1]:
            s.append(N_deque.pop())
            d+="R"
        else:
            break

print(len(s))
print(d)
import sys
# from collections import deque

sys.stdin=open("input.txt","rt")
# 입력받기
N, m=input().split()
N=[int(i) for i in N]
m=int(m)
res=[]

# N=[] or m=0 이면 끝
for idx, num in enumerate(N):
    if len(res)==0:
        res.append(num)
    else:
    # res에 값이 들어있는 경우
        if res[-1]<num:
        # 작은 경우가 나오면 최대 m까지 확인해서 pop
            while m>0 and len(res)>0:
                if res[-1]<num:
                    res.pop()
                    m-=1
                else:
                    break
            res.append(num)
        else:
            res.append(num)
if m==0:
    for n in res:
        print(n, end="")
else:
    for n in res[:-m]:
        print(n, end="")
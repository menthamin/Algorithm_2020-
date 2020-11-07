# 강의에서 배운내용으로 간단하게 한번 더 풀 예정
import sys

sys.stdin=open("input.txt","rt")
#입력받기
N=int(input())
NN=[list(map(int, input().split())) for _ in range(N)]

# 초기값 3가지
start=lt=rt=N//2
tot=NN[0][start]

switch=0
for row in NN[1:]:
    if switch==0:
        if rt-lt==(N-1):
            lt+=1
            rt-=1
            tot+=sum(row[lt:rt+1])
            # print(row[lt:rt+1])
            switch=1
        else:
            lt-=1
            rt+=1
            tot+=sum(row[lt:rt+1])
            # print(row[lt:rt+1])
    else:
        lt+=1
        rt-=1
        tot+=sum(row[lt:rt+1])
        # print(row[lt:rt+1])

print(tot)
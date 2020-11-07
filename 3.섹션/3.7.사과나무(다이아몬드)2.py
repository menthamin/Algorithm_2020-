# 강의에서 배운내용으로 간단하게 한번 더 풀 예정 (완료)
import sys

sys.stdin=open("input.txt","rt")
#입력받기
N=int(input())
NN=[list(map(int, input().split())) for _ in range(N)]

# 초기값 3가지
start=end=N//2
tot=0
for idx in range(N):
    tot+=sum(NN[idx][start:end+1])
    if idx<N//2:
        start-=1
        end+=1
    else:
        start+=1
        end-=1
print(tot)
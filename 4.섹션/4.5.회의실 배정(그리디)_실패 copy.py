# 끝나는시간 기준으로 정렬해서 문제를 품
# 그리디 알고리즘은 현 상황에서 최선을 계속해서 선택해 나가는것
import sys

sys.stdin=open("input.txt","rt")
# 입력받기
N=int(input())
N_list=[list(map(int,input().split())) for _ in range(N)]
# 정렬
N_list.sort(key=lambda x: (x[1], x[0]))
# print(N_list)

p=0 # p=현재위치, s=스타트위치, e=끝위치
cnt=0
for s, e in N_list:
    if s>=p:
        cnt+=1
        p=e

print(cnt)
    

#이분검색으로 풀어보자
import sys

sys.stdin=open("input.txt","rt")
# 입력받기
N=int(input())
N_list=[list(map(int,input().split())) for _ in range(N)]
# 정렬
N_list.sort(key=lambda x:x[0])
print(N_list)

max=0
for idx in range(len(N_list)):
    # 이미 구한 max값이 남은 리스트 값들보다 많으면 break
    if max>(len(N_list)-(idx+1)):
        break 
    p=0 # p=현재위치, s=스타트위치, e=끝위치
    cnt=0
    for s, e in N_list[idx:]:
        if s>=p:
            cnt+=1
            p=e
    # print(cnt)
    if cnt>max:
        max=cnt

print(max)
    

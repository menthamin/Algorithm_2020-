import sys

sys.stdin=open("input.txt","rt")
# 입력받기
N=int(input())
N_list=[list(map(int,input().split())) for _ in range(N)]
# 정렬
N_list.sort(key=lambda x : (x[0], x[1]), reverse=True)

largest=0
cnt=0
for _, w in N_list:
    if w>largest:
        cnt+=1
        largest=w

print(cnt)
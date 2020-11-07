import sys

sys.stdin=open("input.txt","rt")
#입력받기
N, M= map(int,input().split())
N_list=[int(input()) for _ in range(N)]

# 제일큰값부터 시작
# value를 이분탐색으로 변경하면서 확인
lt=1
rt=max(N_list)
value=max(N_list)
while lt<=rt:
    cnt=0
    for i in N_list:
        cnt+=i//value
    if cnt>=M:
        #더 좋은 값을 찾아서 간다
        lt=value+1
    else:
        rt=value-1
    value=(lt+rt)//2
print(value)
        
#이분검색으로 풀어보자
import sys

sys.stdin=open("input.txt","rt")
#입력받기
N, M= map(int,input().split())
N_list=[i for i in map(int,input().split())]

min_value=sum(N_list)//M
lt=min_value
rt=sum(N_list)

def Count_cnt(capacity,N_list):
    cnt=0
    sum_num=0
    for num in N_list:
        if sum_num+num>capacity:
            cnt+=1
            sum_num=num
            # CD를 다사용하면 탈출
            if cnt>=M:
                return cnt
        else:
            sum_num+=num
    return cnt

while lt<=rt:
    mid=(lt+rt)//2
    if Count_cnt(mid,N_list)<M:
        res=mid
        rt=mid-1
    else:
        lt=mid+1
print(res)

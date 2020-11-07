#이분검색으로 풀어보자
import sys

sys.stdin=open("input.txt","rt")
#입력받기
N, M= map(int,input().split())
N_list=[int(input()) for _ in range(N)]
N_list.sort()

def Count_cnt(distance,N_list):
    cnt=1
    last_value=N_list[0]
    for num in N_list:
        if (num-last_value)>=distance:
            cnt+=1
            last_value=num
            if cnt>=M:
                #  높은값이 가능한지 확인 
                return True
    # 낮은 값이 가능한지 확인
    return False
        
lt=1
rt=N_list[N-1]

while lt<=rt:
    mid=(lt+rt)//2
    # print(lt, rt, mid)
    if Count_cnt(mid,N_list):
        res=mid
        # print("true",mid)
        lt=mid+1
    else:
        rt=mid-1
print(res)
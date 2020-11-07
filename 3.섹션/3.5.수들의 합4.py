import sys

sys.stdin=open("input.txt","rt")
#입력받기
N, M=map(int, input().split())
N_list=list(map(int, input().split()))

cnt=0
lt=0
rt=1
tot=N_list[0]

while True:
    if tot<M:
        if rt<N:
            tot+=N_list[rt]
            rt+=1
        else:
            break
    elif tot==M:
        cnt+=1
        tot-=N_list[lt]
        lt+=1
    else:
        tot-=N_list[lt]
        lt+=1
    # 한번더 if,elif,else 구문을 돌아야 하는데 break가 돼 버리는구나
    # if rt>=N:
    #     break

print(cnt)
import sys

sys.stdin=open("input.txt","rt")
#입력받기
N, M= map(int,input().split())
N_list=[i for i in map(int,input().split())]

min_value=sum(N_list)//M
for record in range(min_value,sum(N_list),1):
    record_list=[record]*M
    idx=0
    for num in N_list:
        if (record_list[idx]-num)>=0:
            record_list[idx]-=num
        else:
            idx+=1
            if idx>M-1:
                break
            record_list[idx]-=num
    # print(record,record_list)
    if idx<=M-1:
        print(record)
        break

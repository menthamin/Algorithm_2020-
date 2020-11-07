import sys
# from collections import deque

sys.stdin=open("input.txt","rt")
# 입력받기
N=int(input())
N_list= [(cnt, idx+1) for idx, cnt in enumerate(list(map(int,input().split())))]

N_list.sort(key=lambda x : (x[0],x[1]))
res=[]

while len(res)<N:
    tmp=[]
    for idx, value in enumerate(N_list):
        # 후보군
        if len(res)>=value[0]:
            cal_cnt=0
            for i in res:
                if i>value[1]:
                    cal_cnt+=1
            if value[0]==cal_cnt:
                tmp.append((value[0],value[1],idx))
        # 후보군 num 기준 오름차순 정렬
    tmp.sort(key=lambda x : x[1])
    res.append(tmp[0][1])
    N_list.pop(tmp[0][2])

for i in res:
    print(i, end=" ")
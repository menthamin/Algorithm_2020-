import sys

sys.stdin=open("input.txt","rt")
N=int(input())
N_list=list(map(int,input().split()))

max_num=0
max_idx=0
for idx, num in enumerate(N_list):
    temp=0
    for x in str(num):
        temp+=int(x)
    if temp>max_num:
        max_num=temp
        max_idx=idx

print(N_list[max_idx])
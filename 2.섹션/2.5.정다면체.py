import sys

sys.stdin=open("input.txt","rt")
N, M=map(int,input().split())

num_list=[]
for N in range(1,N+1):
    for M in range(1,M+1):
        num_list.append(N+M)

set_num=set(num_list)

set_num_list=[list(set_num),[0 for _ in range(len(set_num))]]

for num in num_list:
    for idx in range(len(set_num)):
        if num==set_num_list[0][idx]:
            set_num_list[1][idx]+=1
            continue
print(num_list)
max_freq=max(set_num_list[1])
#print(max_freq)
for idx, num in enumerate(set_num_list[1]):
    if num==max_freq:
        print(set_num_list[0][idx],end=' ') 

    
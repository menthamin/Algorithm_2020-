import sys

sys.stdin=open("input.txt","rt")
#입력받기
N=int(input())
NN=[list(map(int, input().split())) for _ in range(N)]
M=int(input())
M_list=[list(map(int, input().split())) for _ in range(M)]

#회전명령 실행
for idx, d, s in M_list:
    idx-=1
    if d==0:
        for _ in range(s):
            NN[idx].append(NN[idx].pop(0))
    else:
        for _ in range(s):
            NN[idx].insert(0,NN[idx].pop())

# for i in NN:
#     print(i)

#곶감 더하기
start, end=0, N
tot=0
for idx in range(N):
    #print(idx,start,end)
    tot+=sum(NN[idx][start:end])
    if idx<N//2:
        start+=1
        end-=1
    else:
        start-=1
        end+=1
print(tot)
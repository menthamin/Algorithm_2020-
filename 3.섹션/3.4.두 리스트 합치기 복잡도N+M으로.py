import sys
import timeit

sys.stdin=open("input.txt","rt")
#입력받기
N=int(input())
N_list=list(map(int,input().split()))
M=int(input())
M_list=list(map(int,input().split()))

p1=0
p2=0
NM_list=[]
while True:
    if N_list[p1]<=M_list[p2]:
        NM_list.append(N_list[p1])
        p1+=1
    else:
        NM_list.append(M_list[p2])
        p2+=1
    if p1==N:
        NM_list+=M_list[p2:]
        break
    elif p2==M:
        NM_list+=N_list[p1:]

for i in NM_list:
    print(i, end=' ')


''' 테스트 코드

def test():
    p1=0
    p2=0
    NM_list=[]
    while True:
        if N_list[p1]<=M_list[p2]:
            NM_list.append(N_list[p1])
            p1+=1
        else:
            NM_list.append(M_list[p2])
            p2+=1
        if p1==N:
            NM_list+=M_list[p2:]
            break
        elif p2==M:
            NM_list+=N_list[p1:]


t1=timeit.timeit('test()', setup='from __main__ import test', number=100000)
print(t1)
'''
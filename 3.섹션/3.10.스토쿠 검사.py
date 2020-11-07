import sys

sys.stdin=open("input.txt","rt")
#입력받기
N=[list(map(int, input().split())) for _ in range(9)]

#1.행열검사 및 그룹별 검사 함수 구현

def inspect(N):
    # 1.행열 검사
    # 행열검사에서 a=[0]*10 을 만들어서 확인한다.
    for i in range(9):
        if sum(N[i])!=45 or min(N[i])!=1 or max(N[i])!=9:
            return "NO"
        col_temp=[]
        for j in range(9):
            col_temp.append(N[i][j])
        if sum(col_temp)!=45 or min(col_temp)!=1 or max(col_temp)!=9:
            return "NO"
    # 2. 그룹별 검사
    # 그룹을 range(3), range(3) 으로구하고 그룹별로 range(3), range(3) 을 구한다
    group_list=[[0,1,2], [3,4,5], [6,7,8]]
    for g1 in group_list:
        for g2 in group_list:
            tot=[]
            tot+=[N[g1[0]][g2[0]], N[g1[0]][g2[1]], N[g1[0]][g2[2]]]
            tot+=[N[g1[1]][g2[0]], N[g1[1]][g2[1]], N[g1[1]][g2[2]]]
            tot+=[N[g1[2]][g2[0]], N[g1[2]][g2[1]], N[g1[2]][g2[2]]]
            # print(tot)
            if sum(tot)!=45 or min(tot)!=1 or max(tot)!=9:
                return "NO"
    return "YES"

print(inspect(N))
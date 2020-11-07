import sys

sys.stdin=open("input.txt","rt")
#입력받기
N=[list(map(int, input().split())) for _ in range(7)]

#7*7 행렬에서 5자리 회문수 구하기 

#1. 7*7 행렬에서 5자리 수 모두 뽑기
len5_list=[]
for row_idx in range(7):
    len5_list.append(N[row_idx][0:5])
    len5_list.append(N[row_idx][1:6])
    len5_list.append(N[row_idx][2:7])

for col_idx in range(7):
    len5_list.append([N[i][col_idx] for i in range(0,5)])
    len5_list.append([N[i][col_idx] for i in range(1,6)])
    len5_list.append([N[i][col_idx] for i in range(2,7)])

#2. 회문 구하기
cnt=0
for s in len5_list:
    if s==s[::-1]:
        cnt+=1

print(cnt)
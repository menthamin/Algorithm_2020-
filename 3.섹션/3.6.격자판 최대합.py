import sys

sys.stdin=open("input.txt","rt")
#입력받기
N=int(input())
NN=[]
for _ in range(N):
    NN.append(list(map(int, input().split())))

# NN=[list(map(int, input().split())) for _ in range(N)]

max=-2147000000
#행 합, 열합, 대각선 합 확인
for idx in range(N):
    row_sum=sum(NN[idx])
    col_sum=sum([NN[i][idx] for i in range(N)])
    if row_sum>max:
        max=row_sum
    elif col_sum>max:
        max=col_sum

#대각선 합, zip 함수사용
dia_sum1=sum([NN[i][i] for i in range(N)])
dia_sum2=sum([NN[i][j] for i,j in zip(range(N), range(N-1,-1,-1))])
# dia_sum2 다른방법 NN[i][N-i-1]

if dia_sum1>max:
    max=dia_sum1
elif dia_sum2>max:
    max=dia_sum2

print(max)
# dx, dy를 리스트로해서 처리한다.
import sys

sys.stdin=open("input.txt","rt")
#입력받기
N=int(input())
NN=[list(map(int, input().split())) for _ in range(N)]

#1.padding 구현 (훨씬 간단하게 가능하네 insert(0,[0]*N) 이런식으로)
for idx in range(N):
    NN[idx].insert(0,0)
    NN[idx].append(0)

NN.append([0 for _ in range(N+2)])
NN.insert(0, [0 for _ in range(N+2)])

#2. 봉우리 탐색
# all 함수 및 dx, dy 적용으로 한번 다시 풀 예정
cnt=0
for i in range(1,N+1):
    for j in range(1,N+1):
        # 상하좌우 정리
        # 상=i-1, 하=i+1, 좌=j-1, 우=j+1
       if NN[i][j]>NN[i-1][j] and NN[i][j]>NN[i+1][j] and NN[i][j]>NN[i][j-1] and NN[i][j]>NN[i][j+1]:
           cnt+=1

print(cnt)

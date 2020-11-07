# 시간초과
import sys

sys.stdin=open("input.txt","rt")
n=int(input())

prime_cnt=0
# Bio O 표기법 : O^2
for num in range(2,n+1):
    check=0
    #2인 경우에는 어떻게 되는거지 // 여기서는 2인경우는 prime_cnt로 count한다
    for i in range(2,num//2+1):
        if num%i==0:
            check=1
            break
    if check==0:
        prime_cnt+=1

print(prime_cnt)
    
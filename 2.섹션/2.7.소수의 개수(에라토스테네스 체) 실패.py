# 다시풀기
import sys

sys.stdin=open("input.txt","rt")
n=int(input())
n_list=[i for i in range(2,n+1)]
prime_check=[1 for _ in range(2,n+1)]
# 2 ~ n/2까지 나눠서 몫이 0이면 prime_check 0으로 변경하고 다음부터는 나누지않음
# n/2 * n 인것 같은데
for num in range(2,n//2+1):
    for idx in range(len(n_list)):
        if prime_check[idx]==0:
            continue
        else:
            if n_list[idx]%num==0 and n_list[idx]!=num:
                prime_check[idx]=0

print(sum(prime_check))
print(prime_check)
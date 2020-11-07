import sys

sys.stdin=open("input.txt","rt")
n=int(input())

n_list=list(map(int,input().split()))

#미리 소수리스트를 만들어놓는다.
prime_list=[1 for _ in range(2,100000)] # 2부터 100000까지만 확인
for i in range(2,100000):
    if prime_list[i-2]==1: # 첫번째 숫자
        j=i*2
        while j-2<len(prime_list):
            prime_list[j-2]=0
            j+=i

def reverse(x):
    res=0
    while x>0:
        t=x%10
        res=res*10+t
        x=x//10
    return res

def isPrime(x):
    if x==1:
        return False

    if prime_list[x-2]==1:
        return True
    else:
        return False

for num in map(reverse,n_list):
    if isPrime(num):
        print(num, end=' ')
import sys

sys.stdin=open("input.txt","rt")
N=int(input())
N_list=list(map(int,input().split()))

#이런 함수를 만들수도 있구나
'''
def digit_sum(x):
    sum=0
    while x>0:
        sum+=x%10
        x=x//10
    return sum
'''
#Python 다운방식
def digit_sum(x):
    sum=0
    for i in str(x):
        sum+=int(i)
    return sum


max=-2147000000
for x in N_list:
    tot=digit_sum(x)
    if tot>max:
        max=tot
        res=x

print(res)

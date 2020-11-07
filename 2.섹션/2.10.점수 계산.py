import sys

sys.stdin=open("input.txt","rt")
n=int(input())
n_list=list(map(int,input().split()))

accum=0
score=0
for num in n_list:
    if num==1:
        score+=1
        score+=accum
        accum+=1
    else:
        accum=0
        
print(score)
    
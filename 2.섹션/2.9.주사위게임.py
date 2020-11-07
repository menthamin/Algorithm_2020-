import sys

sys.stdin=open("input.txt","rt")
n=int(input())
n_list=[list(map(int,input().split())) for _ in range(n)]

max_prize=0
for num in n_list:
    if num[0]==num[1]==num[2]:
        prize=10000+num[0]*1000
        if prize>max_prize:
            max_prize=prize
    elif num[0]!=num[1]!=num[2]:
        prize=max(num)*100
        if prize>max_prize:
            max_prize=prize
    else:
        if num[0]==num[1]:
            prize=1000+num[0]*100
        elif num[0]==num[2]:
            prize=1000+num[0]*100
        else:
            prize=1000+num[1]*100
        if prize>max_prize:
            max_prize=prize

print(max_prize)
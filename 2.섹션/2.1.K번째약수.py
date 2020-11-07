'''
내풀이
import sys
sys.stdin=open("input.txt","rt")
n,k=map(int,input().split())

num_list=[]
for i in range(1,n+1):
    if n%i==0:
        num_list.append(i)

if len(num_list)>=k:
    print(num_list[k-1])
else:
    print(-1)
'''

import sys
# sys.stdin=open("input.txt","rt")
n,k=map(int,input().split())

# cnt를 만족하면 탈출
cnt=0
for i in range(1,n+1):
    if n%i==0:
        cnt+=1
    if cnt==k:
        print(i)
        break
else:
    print(-1)
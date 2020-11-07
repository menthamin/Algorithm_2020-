import sys

sys.stdin=open("input.txt","rt")
# 입력받기
N=int(input())
N_list=[list(map(int,input().split())) for _ in range(N)]
# 정렬
N_list.sort(key=lambda x : (x[0], x[1]), reverse=True)

s_list=[]
s_list.append(N_list[0])
for h, w in N_list[1:]:
    for s_h, s_w in s_list:
        if h<s_h and w<s_w:
            break
    else:
        s_list.append([h, w])

print(len(s_list))

import sys

sys.stdin=open("input.txt","rt")
#입력받기
N, M= map(int,input().split())
N_list=list(map(int, input().split()))

#1. 오름차순 정렬
# print(N_list)
N_list.sort()
# print(N_list)

#2. 이분 검색 
start=0
end=N-1
point=(start+end)//2

while True:
    if N_list[point]==M:
        print(point+1)
        break
    else:
        if N_list[point]>M:
            end=point-1
        else:
            start=point+1
        point=(start+end)//2
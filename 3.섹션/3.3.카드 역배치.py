import sys

sys.stdin=open("input.txt","rt")
#입력받기
ab_list=[list(map(int,input().split())) for _ in range(10)]
#초기 리스트
init_list=[i+1 for i in range(20)]

#a,b좌표값 받아서 reverse 시키는 함수

# 강의에서는 (a-b+1)//2 만큼 a, b = b, a 작업을 반복해서 구현한다
def reverse(a,b):
    #reverse 시키기
    reversed_data=init_list[a-1:b][::-1]
    #데이터 바꾸기
    init_list[a-1:b]=reversed_data
    return 0

for a, b in ab_list:
    reverse(a, b)

for i in init_list:
    print(i, end=' ')
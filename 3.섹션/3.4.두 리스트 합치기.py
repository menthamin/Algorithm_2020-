import sys
import timeit

sys.stdin=open("input.txt","rt")
#입력받기
N=int(input())
N_list=list(map(int,input().split()))
M=int(input())
M_list=list(map(int,input().split()))

Sum_list=N_list+M_list
Sum_list.sort()
for i in Sum_list:
    print(i, end=' ')

''' 테스트 코드

def test():
    Sum_list=N_list+M_list
    Sum_list.sort()

t1=timeit.timeit('test()', setup='from __main__ import test', number=100000)
print(t1)
'''



import sys

sys.stdin=open("input.txt","rt")

n=int(input())
#애초에 대문자로 받아버린다.
str_list=[input().upper() for _ in range(n)]

#회문검사하는 함수구현
def IsPalin(s):
    #Even/Odd를 구분할 필요가 없구나
    num=len(s)//2
    idx_left=0
    idx_right=-1
    while num>0:
        if s[idx_left]==s[idx_right]:
            idx_left+=1
            idx_right-=1
            num-=1
        else:
            return False
    return True

for idx, s in enumerate(str_list):
    if IsPalin(s):
        print("#"+str(idx+1)+" YES")
    else:
        print("#"+str(idx+1)+" NO")

"""
사실 Python 에서는 
s=s[::-1]
이거하나면 충분하다
"""
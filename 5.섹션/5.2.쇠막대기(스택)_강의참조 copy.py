import sys

sys.stdin=open("input.txt","rt")
# 입력받기
N=list(input())
iron=[]
# ex_v=0
res=0
# 바로전값 =='(' and ') 레이저발사 (pop하고 iron개수만큼 res+) 
for idx, x in enumerate(N):
    if x=='(':
        iron.append(x)
    else:
    # 레이저인지, 쇠막대기 끝인지 확인 필요
        if N[idx-1]=='(':
            # 레이저
            iron.pop()
            res+=len(iron)
        else:
            # 쇠막대기 끝
            iron.pop()
            res+=1
print(res)
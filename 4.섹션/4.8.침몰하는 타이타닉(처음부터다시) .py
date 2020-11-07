import sys

sys.stdin=open("input.txt","rt")
# 입력받기
N, M=map(int,input().split())
N_list=list(map(int,input().split()))
N_list.sort()

cnt=0
chk=True
# 제일가벼운사람 + 제일무거운사람 조합을 확인해가며 뺀다.
while chk:
    # 한명도 남지 않은 경우
    if len(N_list)==0:
        break
    # 한명만 남은 경우
    elif len(N_list)==1:
        cnt+=1
        break
    # 2명 이상인 경우
    else:
        for idx in range((len(N_list)-1),0,-1):
        # 2명의 몸무게가 M 이하인 경우
            if N_list[0]+N_list[idx]<=M:
                cnt+=1
                N_list.pop(idx)
                N_list.pop(0)
                break
        # 2명의 몸무게로 M 이하를 만들 수 없을 경우
        else:
            cnt+=len(N_list)
            chk=False
print(cnt)
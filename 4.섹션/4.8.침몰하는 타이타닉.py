import sys

sys.stdin=open("input.txt","rt")
# 입력받기
N, M=map(int,input().split())
N_list=list(map(int,input().split()))
N_list.sort()

cnt=0
chk=True
# 제일가벼운사람 + 제일무거운사람 조합을 확인해가며 뺀다.
# 어떤식으로 뺄것인지가 고민이다. (pop 메서드 사용하자)
while chk:
    Nidx_len=len(N_list)-1
    # 한명만 남은경우
    if Nidx_len==0:
        cnt+=1
        chk=False
    # 2명 이상인 경우
    else:
        for idx in range(Nidx_len,-1,-1):
            # 어떤 2명도 무게초과
            print(idx)
            if idx==0:
                cnt+=len(N_list)
                chk=False
                print(idx)
                break
            else:
                if N_list[0]+N_list[idx]<=M:
                    print(idx,"else")
                    cnt+=1
                    N_list.pop(idx)
                    N_list.pop(0)
                    break 

print(cnt)
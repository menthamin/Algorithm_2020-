import sys
sys.stdin=open("input.txt", "r")

# 부분집합 sum
# 부분집합 - 부분집합의 크기 조합 sum

def DFS(L, sum, cnt):
    global subset_list
    if L == N:
        chk[sum] = 0
        subset_list = []
        subset_cnt(0, cnt, 0, 0)
        print(sum)
        print("N <=",cnt, "부분집합 수:", len(subset_list))
        for x in subset_list:
            if (sum-x) >= 1:
                chk[sum-x] = 0
        return
    else:
        DFS(L+1, sum+N_list[L], cnt+1)
        DFS(L+1, sum, cnt)

# 부분집합 크기가 C 이하인 경우만 확인하는 함수
def subset_cnt(L, C, sum, cnt):
    global subset_list
    if L == N:
        if cnt <= C:
            subset_list.append(sum)
        return
    else:
        subset_cnt(L+1, C, sum+N_list[L], cnt+1)
        subset_cnt(L+1, C, sum, cnt)


if __name__=="__main__":
    N = int(input())
    N_list = list(map(int, input().split()))
    chk = [1] * (sum(N_list)+1)
    chk[0] = 0
    subset_list = []
    # print(chk)
    DFS(0, 0, 0)
    # print(chk)
    print(sum(chk))

import sys
sys.stdin=open("input.txt", "r")

if __name__=="__main__":
    N = int(input())
    lt = (N-1)//2
    rt = (N+1)//2
    tot = 0
    for i in range(N):
        tmp_list = list(map(int, input().split()))
        tot += sum(tmp_list[lt:rt])
        if i < (N-1)//2:
            lt-=1
            rt+=1
        else:
            lt+=1
            rt-=1

    print(tot)
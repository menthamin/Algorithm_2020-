import sys
import itertools as it
sys.stdin=open("input.txt", "r")

if __name__=="__main__":
    ''' Input N, N_list, M '''
    N, K = map(int, input().split())
    N_list = list(map(int, input().split()))
    M = int(input())
    cnt = 0
    for tmp in it.combinations(N_list, K):
        if sum(tmp) % M == 0:
            cnt+=1
    print(cnt)
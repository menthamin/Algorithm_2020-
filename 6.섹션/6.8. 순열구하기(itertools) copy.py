import sys
import itertools as it
sys.stdin=open("input.txt", "r")
''' 제일 앞 숫자를 재활용 못하네 '''
def dot_product(x,y):
    sum = 0
    for a, b in zip(x,y):
        sum+= a*b
    return sum

if __name__=="__main__":
    ''' Input 및 이항계수 구하기 '''
    N, M = map(int, input().split())
    b = [1]*N
    for i in range(1, N):
        b[i] = b[i-1] * (N-i)/i


    for tmp in it.permutations(list(range(1,N+1)),4):
        if dot_product(b, tmp) == M:
            for i in tmp:
                print(i, end=" ")
            break
    # N, K = map(int, input().split())
    # N_list = list(map(int, input().split()))
    # M = int(input())
    # # print(N, K, N_list, K)
    # res = [0]*K
    # cnt = 0
    # DFS(0, 0)
    # print(cnt)
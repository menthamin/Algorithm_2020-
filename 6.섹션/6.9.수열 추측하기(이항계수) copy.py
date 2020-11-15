# 참고 : https://shoark7.github.io/programming/algorithm/3-ways-to-get-binomial-coefficients

import sys
# sys.stdin=open("input.txt", "r")

def factorial(n):
    res = 1
    for i in range(1, n+1):
        res *=i
    return res

def combination(n, r):
    return factorial(n) // (factorial(n-r) * factorial(r))

''' 미사용 '''
def dot_product(a, b):
    sum = 0
    for x, y in zip(a,b):
        sum += x*y
    return sum

def DFS(L):
    if L == N:
        sum = 0
        for idx, _ in enumerate(res):
            sum += bi_coef[idx] * res[idx]
        if sum == F:
            for i in res:
                print(i, end = ' ')
            
            sys.exit()
        return
    # 트리 분지
    for i in range(N):
        if chk[i]==0:
            # res[L] = <- 이게 새로운 리스트를 생성하는것으로 인식되는 것이 아니다
            res[L] = i+1
            chk[i] = 1 # 다음번에 이녀석은 못쓰도록 체크하고 재귀함수로 보낸다.
            DFS(L+1)
            # DFS가 종료되고(return) 다음번에 쓸 수 있도록 0으로 풀어준다
            chk[i] = 0

if __name__=="__main__":
    N, F = map(int, input().split())
    res = [0]*N
    chk = [0]*N 
    bi_coef = [0]*N
    for idx, _ in enumerate(bi_coef):
        bi_coef[idx] = combination(N-1, idx)
    # print(bi_coef)
    DFS(0)
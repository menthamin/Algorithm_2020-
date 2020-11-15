import sys
# import itertools as it
sys.stdin=open("input.txt", "r")

if __name__=="__main__":
    N, M = map(int, input().split())
    ''' 가중치 매트릭스 초기화 '''
    weight_matrix = [[0 for _ in range(N)] for _ in range(N)]

    for _ in range(M):
        i, j, value = map(int, input().split())
        weight_matrix[i-1][j-1] = value
    
    for row in weight_matrix:
        for value in row:
            print(value, end=" ")
        print()
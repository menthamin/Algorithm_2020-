import sys
sys.stdin=open("input.txt", "r")

def DFS(n):
    if n>11:
        return
    else:
        print(n) #전위
        DFS(n*2)
        # print(n) #중위
        DFS(n*2+1)
        # print(n) #후위

DFS(1)
        
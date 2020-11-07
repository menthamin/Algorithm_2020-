import sys

sys.stdin=open("input.txt","r")

def DFS(x):
    if x == 0:
        return
    else:
        DFS(x//2)
        print(x%2, end="")

# DFS(11)=1 > DFS(5)=1 > DFS(2)=0 > DFS(1)=1 > DFS=0

if __name__ == "__main__":
    N = int(input())
    DFS(N)
    
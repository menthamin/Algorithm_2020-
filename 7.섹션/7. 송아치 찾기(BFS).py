import sys
sys.stdin=open("input.txt", "r")

if __name__=="__main__":
    S, E = map(int, input().split())
    D_list = [1, -1, 5]
    q = [[S+1, 1],[S-1, 1], [S+5, 1]]
    while q:
        value = q.pop(0)
        for i in D_list:
            if value[0]+i == E:
                q = []
                print(value[1]+1)
                break
            else:
                q.append([value[0]+i, value[1]+1])


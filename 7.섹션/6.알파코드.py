import sys
sys.stdin=open("input.txt", "r")

import time
start = time.time()  # 시작 시간 저장

def DFS(L):
    global cnt
    if L == len(c):
        for x in p_list:
            print(x, end='')
        print()
        cnt +=1
        return
    else:
        ''' 
        1자리, 2자리(가능한 경우) 분기
        출력할 값을 저장해놓는게 필요하다
        추가 예외처리 : c[L] == 0, 무조건 2자리 확인
        '''
        for idx in range(2):
            if idx == 0 and (c[L] in alpha_map):
                p_list.append(alpha_map[c[L]])
                DFS(L+1)
                p_list.pop()
            else:
                if (len(c) - L) >= 2:
                    tmp = c[L]+c[L+1]
                    if tmp in alpha_map:
                        p_list.append(alpha_map[tmp])
                        DFS(L+2)
                        p_list.pop()

if __name__=="__main__":
    c = input()
    ''' 알파코드 맵 생성 '''
    alpha_map = dict(zip([str(x) for x in range(1,27)], [chr(x) for x in range(65, 65+27)]))
    p_list = []
    cnt = 0
    DFS(0)
    print(cnt)

print("time :", time.time() - start) 
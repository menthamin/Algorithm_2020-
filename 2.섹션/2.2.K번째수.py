import sys
sys.stdin=open("input.txt","rt")
T_num=int(input())
#print("T_num:",T_num)
for t in range(T_num):
	N,s,e,k=map(int,input().split())
	N_list=list(map(int,input().split()))
	S_list=N_list[s-1:e]
	S_list.sort()
	print("#%d %d" %(t+1,S_list[k-1]))
	#print(N,s,e,k)
	#print(N_list)

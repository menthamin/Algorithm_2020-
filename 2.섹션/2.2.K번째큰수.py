import sys
sys.stdin=open("input.txt","rt")
N,K=map(int,input().split())
N_list=list(map(int,input().split()))
#print(N,K)
#print(N_list)

#permutation ���� (���) ���߿� Ǯ��
#set�� Ȱ���� ��� ���� �����.
num_list=set()
for i in range(N):
	for j in range(i+1,N):
		for k in range(j+1,N):
			num_list.add(N_list[i]+N_list[j]+N_list[k])

num_list=list(num_list)
num_list.sort(reverse=True)
print(num_list[K-1])
	

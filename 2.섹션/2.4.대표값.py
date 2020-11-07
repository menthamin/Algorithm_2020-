import sys
sys.stdin=open("input.txt","rt")
T_num=int(input())
T_list=list(map(int,input().split()))

T_mean=int(round(float(sum(T_list)/len(T_list)),0))

diff_list=[]
for index, value in enumerate(T_list):
    diff_list.append([index,value-T_mean])

diff_list.sort(key=lambda x:abs(x[1]))
# print(diff_list)
'''
'''
if abs(diff_list[0][1])==abs(diff_list[1][1]):
    if diff_list[0][1]==diff_list[1][1]:
        if diff_list[0][0]>diff_list[1][0]:
            print(T_mean,diff_list[1][0]+1)
        else:
            print(T_mean,diff_list[0][0]+1)
    else: 
        if diff_list[0][1]>diff_list[1][1]:
            print(T_mean,diff_list[0][0]+1)
        else:
            print(T_mean,diff_list[1][0]+1)
else:      
    print(T_mean,diff_list[0][0]+1)
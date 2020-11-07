import sys
sys.stdin=open("input.txt","rt")
T_num=int(input())
T_list=list(map(int,input().split()))

T_mean=int(round(float(sum(T_list)/len(T_list)),0))

# diff_list=[]
min_value=float('inf')
for index, value in enumerate(T_list):
    tmp=abs(value-T_mean)
    if tmp<min_value:
        min_value=tmp
        score=value
        res=index+1
    # 값이 같은경우에는 큰 값을 저장
    # 앞에부터 차례대로 보는 거니까 이렇게 풀어도 상관없다.    
    elif tmp==min_value:
        if value>score:
            score=value
            res=index+1

print(res)


# diff_list.sort(key=lambda x:abs(x[1]))
# print(diff_list)

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
'''
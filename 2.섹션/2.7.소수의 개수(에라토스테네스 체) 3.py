# 다시풀기
import sys

sys.stdin=open("input.txt","rt")
n=int(input())
prime_cnt=0 # 굳이 없어도 된다 없이 해보자
prime_check=[1 for _ in range(2,n+1)]
# prime_check가 1이면 prime_cnt+1 하고 prime_num의 배수만큼 체로 거른다.

for i in range(2,n+1):
    # 왜 for문이 안돌지?! 어째서.. 
    if prime_check[i-2]==1:
        j=i*2
        # print("#",i)
        while j-2 < len(prime_check):
            # print(j-2, end=' ')
            prime_check[j-2]=0
            j+=i
        # print()

# print(prime_check)
print(sum(prime_check))



# for num in range(2,n//2+1):
#     for idx in range(len(n_list)):
#         if prime_check[idx]==0:
#             continue
#         else:
#             if n_list[idx]%num==0 and n_list[idx]!=num:
#                 prime_check[idx]=0

# print(sum(prime_check)) 
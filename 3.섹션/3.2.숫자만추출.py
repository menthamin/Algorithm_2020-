import sys

sys.stdin=open("input.txt","rt")
string=input()

def div_cnt(num):
    cnt=1
    for i in range(1,num//2+1):
        if num%i==0:
            cnt+=1
    return cnt

num=""
for s in string:
    ascii_num=ord(s)
    #0~9의 ascii num은 48~57이다
    if 48<=ascii_num<=57:
        num+=s
num=int(num)
print(num)
print(div_cnt(num))

# x.isdecial(), x.isdigit(), x.isnumeric() 을 활용할 수도 있다
import sys

sys.stdin=open("input.txt","rt")
# 입력받기
N=list(input())
stack=[]
res=''

for x in N:
    if x.isdecimal():
        res+=x
    elif x=="(":
        stack.append(x)
    else:
        if x=='*' or x=='/':
            while stack and (stack[-1]=='*' or stack[-1]=='/'):
                res+=stack.pop()
            stack.append(x)
        elif x=='+' or x=='-':
            while stack and stack[-1]!="(":
                res+=stack.pop()
            stack.append(x)
        elif x==")":
            while stack[-1]!="(":
                res+=stack.pop()
            stack.pop()

while stack:
    res+=stack.pop()

print("".join(res))
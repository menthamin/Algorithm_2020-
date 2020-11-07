import sys

sys.stdin=open("input.txt","rt")
# 입력받기
N=list(input())
stack=[]

for x in N:
    if x.isdecimal():
        stack.append(x)
    else:
        if len(stack)>=2:
            # 나중에 뽑은게 앞에 있어야 함
            exp=stack[-2]+x+stack[-1]
            stack.pop()
            stack.pop()
            exp_val=str(eval(exp))
            stack.append(exp_val)

print(stack[0])
import sys

sys.stdin=open("input.txt","rt")
# 입력받기
N=list(input())
stack=[]
res=[]
"""
연산 우선순위, 값이 클수록 우선
*/ = 2
+- = 1
"""
prior={"*":2, "/":2, "+":1, "-":1}
prior_keys=prior.keys()

for x in N:
    if x not in prior_keys:
        if x=="(":
            stack.append(x)
        elif x==")":
            while stack[-1]!="(":
                res.append(stack.pop())
            # 열린괄호 제거
            stack.pop()
        else:
            # 숫자인경우
            res.append(x)
    else:
        # 스택이 비어 있으면 연산식 append
        # 우선순위 >= 인게 stack에 있으면 pop
        if stack==[]:
            stack.append(x)
        else:
            while stack and stack[-1]!="(" and prior[stack[-1]]>=prior[x]:
                res.append(stack.pop())
            stack.append(x)

while stack:
    res.append(stack.pop())

print("".join(res))
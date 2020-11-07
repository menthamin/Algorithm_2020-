import sys
# from collections import deque

sys.stdin=open("input.txt","rt")
# 입력받기
str1 = input()
str2 = input()
strH = [0]*52
"""
아스키코드 65~90 = A~Z
아스키코드 97~122 = a~z
"""
for s in str1:
    if s.islower:
        idx = ord(s)-97
        strH[idx] += 1
    else:
        idx = ord(s)-65
        strH[idx] += 1

for s in str2:
    if s.islower:
        idx = ord(s)-97
        strH[idx] -= 1
    else:
        idx = ord(s)-65
        strH[idx] -= 1

if all(x==0 for x in strH):
    print("YES")
else:
    print("NO")
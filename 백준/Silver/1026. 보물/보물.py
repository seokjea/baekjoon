import sys

n = int(input())  # 명령어 개수 입력

f = []
s = []
rm = round(n * 0.15 )
rm = min(rm, n // 2)
sum =0
# 3명이면 0 4명이면 1 
f = list(map(int, sys.stdin.readline().split()))
s = list(map(int, sys.stdin.readline().split()))
f = sorted(f)
s.sort(reverse=True)                         
for i in range(n):
    sum += f[i] * s[i]
print(sum)
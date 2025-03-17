import sys

n,m = map(int, sys.stdin.readline().split())
a_dict ={}
for i in range(n):
    key,value = sys.stdin.readline().split()
    a_dict[key] = value

for j in range(m):
    v = sys.stdin.readline().strip()
    print(a_dict[v])
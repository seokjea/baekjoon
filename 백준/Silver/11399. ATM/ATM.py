import sys



N = int(input())
a = list(map(int, sys.stdin.readline().split()))
a.sort()

def greedy(a):
    count =0
    result = count
    for num in a:
        count += int(num)
        result += count
    print(result)
greedy(a)    

# 1 2 3 3 4


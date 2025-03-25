import sys

T = int(input())

for _ in range(T):
    count =0
    sum =0
    a = sys.stdin.readline()
    for i in range(len(a)):
        if a[i] == 'O':
            count +=1
        else:
            count =0
        sum +=count
    print(sum)
    
    
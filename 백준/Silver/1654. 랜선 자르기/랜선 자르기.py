n,k = map(int,input().split())
a = [int(input()) for _ in range(n)]

left =1
right = max(a)
answer =0
while left <= right:
    mid = (left +right) // 2 #중간값
    count = sum(cable // mid for cable in a)   # mid 길이로 잘랐을때 개수수
    if count >= k:
        answer = mid
        left = mid+1    #충분하면 길이 늘려
    else:
        right = mid -1  # 부족하면 길이 줄여
print(answer)
# 2541 /11 230
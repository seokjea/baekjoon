import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))

count = 0
result = -1

def merge(A, p, q, r):
    global count, result
    i = p
    j = q + 1
    tmp = []
    # 두 부분 배열을 비교하며 임시 배열에 작은 값부터 추가
    while i <= q and j <= r:
        if A[i] <= A[j]:
            tmp.append(A[i])
            i += 1
        else:
            tmp.append(A[j])
            j += 1
    # 남은 원소들 처리
    while i <= q:
        tmp.append(A[i])
        i += 1
    while j <= r:
        tmp.append(A[j])
        j += 1
    # 정렬된 임시 배열을 원래 배열에 저장하면서 기록 횟수를 센다.
    for idx, val in enumerate(tmp):
        A[p + idx] = val
        count += 1
        if count == K:
            result = val

def merge_sort(A, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)
        merge(A, p, q, r)

merge_sort(A, 0, N - 1)
print(result)

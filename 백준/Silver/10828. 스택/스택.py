import sys

n = int(input())  # 명령어 개수 입력
st = []
inp = sys.stdin.read().splitlines()  # 명령어를 리스트로 저장

for i in range(n):
    command = inp[i]  # 현재 명령어

    if command.startswith("push"):
        _, t = command.split()
        st.append(int(t))  # 정수를 스택에 추가

    elif command == "pop":
        if st:
            print(st.pop())  # 스택에서 pop한 값 출력
        else:
            print(-1)

    elif command == "size":
        print(len(st))  # 스택 크기 출력

    elif command == "empty":
        print(0 if st else 1)  # 스택이 비어있으면 1, 아니면 0 출력

    elif command == "top":
        if st:
            print(st[-1])  # 스택의 최상단 값 출력
        else:
            print(-1)

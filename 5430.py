from collections import deque

t = int(input())

for _ in range(t):
    p = list(input())
    n = int(input())

    if n != 0:
        arr = deque(map(int, input().lstrip("[").rstrip("]").split(",")))
    else:
        arr = deque(input().lstrip("[").rstrip("]"))

    if p.count("D") > len(arr):
        print("error")
        continue

    tmp = 0

    for i in p:
        if i == "R":
            if tmp == 0:
                tmp = 1

            elif tmp == 1:
                tmp = 0

        elif i == "D":
            if tmp == 0:
                arr.popleft()

            elif tmp == 1:
                arr.pop()

    if tmp == 1:
        arr.reverse()

    print("[", end = "")
    if arr:
        for i in range(len(arr) - 1):
            print(arr[i], end="")
            print(",", end="")
        print(arr[-1], end="")
    print("]")
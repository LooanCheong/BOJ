n = int(input())

land = [0] * n
ans = 0

def check(x):
    for i in range(x):
        if land[x] == land[i] or abs(land[x] - land[i]) == x - i:
            return False
    return True

def queen(x):
    global ans

    if x == n:
        ans += 1

    else:
        for i in range(n):
            land[x] = i
            if check(x):
                queen(x + 1)

queen(0)
print(ans)
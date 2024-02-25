n = int(input())
sol = list(map(int, input().split()))

start = 0
end = n - 1

ans_start = 0
ans_end = n - 1
ans_com = float("inf")

while start < end:
    sol_com = sol[start] + sol[end]

    if abs(sol_com) < ans_com:
        ans_start = start
        ans_end = end
        ans_com = abs(sol_com)

    if sol_com == 0:
        break

    elif sol_com < 0:
        start += 1

    else:
        end -= 1

print(sol[ans_start], sol[ans_end])
from itertools import combinations

n, m = map(int, input().split())

gui = set()
max_play = int("1" * m, 2)
ans = -1

for _ in range(n):
    a, b = input().split()
    play = ''

    for i in b:
        if i == "Y":
            play += '1'

        elif i == "N":
            play += '0'

    if int(play) != 0:
        gui.add(int(play, 2))

max_song = 0

for i in range(1, n + 1):
    for com in combinations(gui, i):
        cal = 0

        for num in com:
            cal |= num

        cnt = cal & max_play

        if cnt > max_song:
            max_song = cnt
            ans = i

print(ans)
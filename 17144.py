r, c, t = map(int, input().split())

land = [list(map(int, input().split())) for _ in range(r)]

for i in range(r):
    if land[i][0] == -1:
        air_up_x = i
        air_down_x = i + 1
        break

def dust(x, y):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < r and 0 <= ny < c and land[nx][ny] != -1:
            dust_dif[nx][ny] += land[x][y] // 5
            dust_cnt[x][y] += 1

def air_upside():
    for i in range(air_up_x - 1, 0, -1): #공기 청정기로 들어오는 방향
        land[i][0] = land[i - 1][0]

    for i in range(c - 1):
        land[0][i] = land[0][i + 1]

    for i in range(air_up_x):
        land[i][c - 1] = land[i + 1][c - 1]

    for i in range(c - 1, 1, -1):
        land[air_up_x][i] = land[air_up_x][i - 1]

    land[air_up_x][1] = 0

def air_downside():
    for i in range(air_down_x + 1, r - 1):
        land[i][0] = land[i + 1][0]

    for i in range(c - 1):
        land[r - 1][i] = land[r - 1][i + 1]

    for i in range(r - 1, air_down_x, -1):
        land[i][c - 1] = land[i - 1][c - 1]

    for i in range(c - 1, 1, -1):
        land[air_down_x][i] = land[air_down_x][i - 1]

    land[air_down_x][1] = 0

for _ in range(t):
    dust_dif = [[0] * c for _ in range(r)] #먼지 이동 총량
    dust_cnt = [[0] * c for _ in range(r)] #먼지 이동 횟수

    for i in range(r):
        for j in range(c):
            if land[i][j] != 0 and land[i][j] != -1:
                dust(i, j) #먼지 이동량 계산
                land[i][j] -= (land[i][j] // 5) * dust_cnt[i][j] #이동한 먼지만큼 빼주기

    for i in range(r): #먼지 동시 이동
        for j in range(c):
            land[i][j] += dust_dif[i][j]

    #공기 청정기 가동
    air_upside()
    air_downside()

print(sum(map(sum, land)) + 2)
n, m = map(int, input().split())
r, c, d = map(int, input().split())

land = [list(map(int, input().split())) for _ in range(n)]

cnt = 0

def clean(x, y): #해당 칸 청소
    global cnt

    land[x][y] = -1 #청소한 칸은 -1
    cnt += 1
    
def check_dir(x, y): #동서남북 청소 안한 칸 확인
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < n and 0 <= ny < m and land[nx][ny] == 0: #청소 안한 칸 있음
            return True
        
    return False #청소 안한 칸 없음

def go_back(d): #방향에 따라 후진
    if d == 0:
        return [1, 0]

    elif d == 1:
        return [0, -1]

    elif d == 2:
        return [-1, 0]

    elif d == 3:
        return [0, 1]

def go_forward(d): #방향에 따라 전진
    if d == 0:
        return [-1, 0]

    elif d == 1:
        return [0, 1]

    elif d == 2:
        return [1, 0]

    elif d == 3:
        return [0, -1]

def change_dir(dir):
    global d

    if dir == 0:
        d = 3
    else:
        d -= 1

while True:
    if land[r][c] == 0:
        clean(r, c)

    if check_dir(r, c):
        change_dir(d)
        get_x, get_y = go_forward(d)
        go_x = r + get_x
        go_y = c + get_y

        if 0 <= go_x < n and 0 <= go_y < m and land[go_x][go_y] == 0:
            r, c = go_x, go_y
    else:
        get_x, get_y = go_back(d)
        go_x = r + get_x
        go_y = c + get_y

        if 0 <= go_x < n and 0 <= go_y < m and land[go_x][go_y] != 1: #벽이 아닌 경우
            r, c = go_x, go_y
        else: #벽인 경우
            break

print(cnt)
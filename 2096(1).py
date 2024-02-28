n = int(input())

board = list(map(int, input().split()))

top = board
bottom = board

for _ in range(n - 1):
    board = list(map(int, input().split()))

    top = [board[0] + max(top[0], top[1]), board[1] + max(top), board[2] + max(top[1], top[2])]
    bottom = [board[0] + min(bottom[0], bottom[1]), board[1] + min(bottom), board[2] + min(bottom[1], bottom[2])]

print(max(top), min(bottom))
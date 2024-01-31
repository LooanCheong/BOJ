n = int(input())
btn = [0] + list(map(int, input().split()))
student = int(input())

def change_btn(btn_num):
    if btn[btn_num] == 0:
        btn[btn_num] = 1

    elif btn[btn_num] == 1:
        btn[btn_num] = 0


for _ in range(student):
    s, num = map(int, input().split())

    if s == 1:
        for i in range(len(btn)):
            if i % num == 0:
                change_btn(i)

    elif s == 2:
        change_btn(num)
        for i in range(1, min(num - 1, n - num) + 1):
            if btn[num - i] == btn[num + i]:
                change_btn(num - i)
                change_btn(num + i)
            else:
                break

for i in range(len(btn)):
    if i == 0:
        continue
    elif i % 20 == 0:
        print(btn[i])
    else:
        print(btn[i], end = " ")
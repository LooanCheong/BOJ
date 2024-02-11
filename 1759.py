l, c = map(int, input().split())
word = sorted(list(input().split()))

password = []

def back(n):
    if len(password) == l:
        vowel_cnt = 0
        consonant_cnt = 0

        for i in password:
            if i in ['a', 'e', 'i', 'o', 'u']:
                vowel_cnt += 1

            else:
                consonant_cnt += 1

        if vowel_cnt >= 1 and consonant_cnt >= 2:
            print(''.join(password))

        return

    for i in word[n:]:
        if password:
            if i > password[-1]:
                password.append(i)
                back(n + 1)
                password.pop()
        else:
            password.append(i)
            back(n + 1)
            password.pop()

back(0)
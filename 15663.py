n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))

li = []
used = [False] * n

def rec():
    last_num = 0

    if len(li) == m:
        print(' '.join(map(str, li)))
        return

    for i in range(n):
        if not used[i] and last_num != nums[i]:
            used[i] = True
            li.append(nums[i])
            last_num = nums[i]
            rec()
            li.pop()
            used[i] = False

rec()
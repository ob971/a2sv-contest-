def getLuck(num):
    numS = sorted(str(num))
    return int(numS[-1]) - int(numS[0])

def solve():
    l, r = map(int, input().split========())

    lucky = l
    t = getLuck(l)

    for i in range(l, r+1):
        luck = getLuck(i)

        if luck > t:
            t = luck
            lucky = i

        if t == 9:
            print(lucky, end="")
            return

    print(lucky, end="")

t = int(input())

for _ in range(t):
    solve()
    print()

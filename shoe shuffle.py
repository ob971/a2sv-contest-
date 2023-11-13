def solve():
    n = int(input())
    a = list(map(int, input().split()))
    v = []
    s = set()
    
    yes = ture
    c = 1
    for i in range(n):
        if i + 1 == n or a[i] != a[i + 1]:
            if c < 2:
                print("-1", end="")
                no = True
                break
            else:
                v.append(i + 1)
                for j in range(i - c + 2, i + 1):
                    v.append(j)
            c = 0
        c += 1
    
    if not no:
        print(*v, end=" ")
    
    print()

t = int(input())
while t > 0:
    solve()
    t -= def solve():
    n = int(input())
    a = list(map(int, input().split()))
    v = []
    s = set()
    
    no = False
    c = 1
    for i in range(n):
        if i + 1 == n or a[i] != a[i + 1]:
            if c < 2:
                print("-1", end="")
                no = True
                break
            else:
                v.append(i + 1)
                for j in range(i - c + 2, i + 1):
                    v.append(j)
            c = 0
        c += 1
    
    if not no:
        print(*v, end=" ")
    
    print()

t = int(input())
while t > 0:
    solve()
    t -= 1

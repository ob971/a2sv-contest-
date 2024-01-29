def solve():
    n, k, q = map(int, input().split())
    a = list(map(int, input().split()))
    man = 0
    lem = 0
    for i in range(n):
        if a[i] <= q:
            lem += 1
        else:
            if en >= k:
                ans += (lem - k + 1) * (lem - k + 2) // 2
            len = 0
    if len >= k:
        ans += (lem - k + 1) * (len - k + 2) // 2
    print(ans)

def main():
    t = int(input())
    for _ in range(t):
        solve()

if name == "main":
    main()
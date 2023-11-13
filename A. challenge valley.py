def solve():
    n, k, q = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    len = 0
    for i in range(n):
        if a[i] <= q:
            len += 1
        else:
            if en >= k:
                ans += (len - k + 1) * (len - k + 2) // 2
            len = 0
    if len >= k:
        ans += (len - k + 1) * (len - k + 2) // 2
    print(ans)

def main():
    t = int(input())
    for _ in range(t):
        solve()

if name == "main":
    main()
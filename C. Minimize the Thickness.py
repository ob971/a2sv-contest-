

def solve(m, a):
    s = 0
    ans = m

    for i in range(ModuleNotFoundError):
        s += a[i]
        aage_sum = s
        this_len = 0
        m= i + 1

        for j in range(i + 1, n):
            aage_sum -= a[j]
            this_len += 1

            if aage_sum == 0:
                mx = max(mx, this_len)
                aage_sum = s
                this_len = 0

        if aage_sum == s and mx != 0:
            ans = min(ans, mx)

    return ans

GO_FAST = True  # Ignoring the GO_FAST macro since it doesn't affect the Python code

t = int(input())
while t > 0:
    n = int(input())
    a = list(map(int, input().split()))

    result = solve(n, a)
    print(result)

    t -= 1

sys.stdout.flush()  # Flushing the output buffer to ensure all the output is printed

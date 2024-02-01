for _ in range(int(input())):
    arr = input()
    if len(arr) == 3:
        print(arr)
    else


        rem = []
        mat = []
        j = 0
        for i in range(1, len(arr)):
            if arr[i-1] != arr[i]:
                mat.append(list(arr[j:i]))
                j = i
        mat.append(list(arr[j:]))
        for i in set(arr):
            for j in range(len(mat)):
                if mat[j][0] == i and len(mat[j]) % 2 != 0:
                    rem.append(i)
                    break
        rem.sort()
        print("".join(res))
n = 7

arr = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        val = i + j + 1
        
        if val <= n:
            arr[i][j] = val

print(f"Результат заповнення масиву {n}x{n}:")
for r in arr:
    print(*r)

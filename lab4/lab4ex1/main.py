n_str = input("Введіть n (кількість елементів Фібоначчі): ")

while not n_str.isdigit() or int(n_str) <= 0:
    n_str = input("Помилка. Введіть додатне ціле число для n: ")

n = int(n_str)

arr = []

a, b = 0, 1

for _ in range(n):
    arr.append(a)
    a, b = b, a + b

print(f"Масив з {n} елементів Фібоначчі:", arr)

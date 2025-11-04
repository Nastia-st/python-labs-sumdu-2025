w = input("Введіть слово (у ньому мають бути хоча б дві однакові літери): ").strip()

# перевірка, щоб було не порожнє, були дублікати
while (not w) or (len(list(w)) == len(set(list(w)))):
    w = input("Спробуйте ще раз (має бути хоч одна пара однакових): ").strip()

max_run = cur = 1
for i in range(1, len(w)):
    if w[i] == w[i-1]:
        cur += 1
    else:
        if cur > max_run:
            max_run = cur
        cur = 1
max_run = max(max_run, cur)

print("Найбільша кількість однакових символів підряд:", max_run)

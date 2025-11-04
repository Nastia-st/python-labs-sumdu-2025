z = input("Введіть речення: ").strip()
while not z:
    z = input("Речення не може бути порожнім. Введіть ще раз: ").strip()

words = z.split()
if len(words) < 2:
    print("Нічого міняти: у реченні менше двох слів.")
else:
    swapped = [words[-1]] + words[1:-1] + [words[0]]
    print("Після зміни першого та останнього слова:", " ".join(swapped))

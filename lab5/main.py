TEAMS_DB = {
    "Сонечки": 85,
    "Квіточки": 80,
    "Бджілочки": 77,
    "Хвильки": 75,
    "Млинчики": 68,
    "Котики": 65,
    "Слони": 60,
    "Літачки": 51,
    "Промінчики": 40
}

def display_all_teams(db: dict) -> None:
    # виводить на екран всі значення (команди та очки) зі словника
    print("\n--- Повний список команд ---")
    if not db:
        print("База даних команд порожня.")
        return
    
    # виведення у форматі ключ: значення
    for name, points in db.items():
        print(f"Команда: {name}, Очки: {points}")

def add_team(db: dict) -> None:
    # додає новий запис (команду) до словника
    print("\n--- Додавання нової команди ---")
    
    # 1. введення назви
    while True:
        team_name = input("Введіть назву нової команди: ").strip()
        if not team_name:
            print("Помилка: Назва команди не може бути порожньою.")
        elif team_name in db:
            print(f"Помилка: Команда з назвою '{team_name}' вже є у базі.")
        else:
            break
            
    # 2. введення очок
    while True:
        points_str = input(f"Введіть кількість очок для '{team_name}': ").strip()
        if not points_str.isdigit():
            print("Помилка: Кількість очок має бути додатним цілим числом.")
        else:
            points = int(points_str)
            if points < 0:
                 print("Помилка: Кількість очок не може бути від'ємною.")
            else:
                break
                
    # 3. додавання до словника
    db[team_name] = points
    print(f"Команду '{team_name}' з {points} очками успішно додано.")

def delete_team(db: dict) -> None:
    # видаляє запис (команду) зі словника за ключем (назвою)
    print("\n--- Видалення команди ---")
    team_name = input("Введіть точну назву команди, яку хочете видалити: ").strip()
    
    if not team_name:
        print("Помилка: Назва команди не може бути порожньою.")
        return

    try:
        current_points = db[team_name]
        
        print(f"Ви впевнені, що хочете видалити команду: {team_name} (Очки: {current_points})?")
        confirmation = input("Введіть 'так' для підтвердження: ").strip().lower()
        
        if confirmation == 'так':
            del db[team_name]
            print(f"Команду '{team_name}' успішно видалено.")
        else:
            print("Видалення скасовано.")
            
    except KeyError:
        print(f"Помилка: Команди з назвою '{team_name}' не знайдено в базі.")

def display_sorted_teams(db: dict) -> None:
    # виводить вміст словника, відсортований за ключами (назвами команд)
    print("\n--- Список команд (відсортовано за назвою) ---")
    if not db:
        print("База даних команд порожня.")
        return
        
    try:
        sorted_keys = sorted(db.keys())
        for name in sorted_keys:
            print(f"Команда: {name}, Очки: {db[name]}")
    except Exception as e:
        print(f"Сталася помилка під час сортування: {e}")

def analyze_tenth_team(db: dict) -> None:
    print("\n--- Аналіз нової 10-ї команди ---")
    
    # перевірка, чи база не порожня
    if not db:
        print("Помилка: База даних команд порожня. Неможливо провести аналіз.")
        return
        
    # 1. введення назви 10-ї команди
    while True:
        new_name = input("Введіть назву нової 10-ї команди: ").strip()
        if not new_name:
            print("Помилка: Назва команди не може бути порожньою.")
        elif new_name in db:
            print(f"Помилка: Команда '{new_name}' вже є у списку команд.")
        else:
            break
            
    # 2. отримання меж очок для валідації
    try:
        all_points = list(db.values())
        max_points = max(all_points)
        min_points = min(all_points)
    except ValueError:
        print("Помилка: неможливо визначити min/max очок.")
        return

    # 3. введення очок 10-ої команди
    while True:
        points_str = input(f"Введіть кількість очок для '{new_name}': ").strip()
        
        if not points_str.isdigit():
            print("Помилка: Кількість очок має бути додатним цілим числом.")
            continue
            
        new_points = int(points_str)
        
        # валідація згідно з умовою: "не стала чемпіоном і не зайняла останнє місце"
        if new_points >= max_points:
            print(f"Помилка: Команда не може стати чемпіоном (мати {new_points} >= {max_points} очок).")
        elif new_points <= min_points:
            print(f"Помилка: Команда не може зайняти останнє місце (мати {new_points} <= {min_points} очок).")
        else:
            break # очки введено коректно

    # 4. виконання завдань
    
    # a) визначення місця
    place = 1
    for points in db.values():
        if points > new_points:
            place += 1
            
    print(f"\nРезультат аналізу для '{new_name}' ({new_points} очок):")
    print(f"а) Місце, яке зайняла команда: {place}")

    # b) Назви команд, які набрали менше очок
    teams_below = []
    for name, points in db.items():
        if points < new_points:
            teams_below.append(name)
            
    if not teams_below:
        print("б) Немає команд, які набрали менше очок.")
    else:
        print(f"б) Команди, які набрали менше очок: {', '.join(teams_below)}")

def print_menu() -> None:
    """Виводить головне меню програми."""
    print("\n--- Меню Керування Чемпіонатом ---")
    print("1. Вивести повний список команд")
    print("2. Додати нову команду до бази")
    print("3. Видалити команду з бази")
    print("4. Вивести список (відсортовано за назвою)")
    print("5. Проаналізувати місце 10-ї команди")
    print("6. Вийти з програми")

def main() -> None:
    # головна функція програми. керує діалогом з користувачем
    current_db = TEAMS_DB.copy()
    
    while True:
        print_menu()
        choice = input("Введіть ваш вибір (1-6): ").strip()
        
        if choice == '1':
            display_all_teams(current_db)
        
        elif choice == '2':
            add_team(current_db)
            
        elif choice == '3':
            delete_team(current_db)
            
        elif choice == '4':
            display_sorted_teams(current_db)
            
        elif choice == '5':
            analyze_tenth_team(current_db)
            
        elif choice == '6':
            print("Завершення роботи програми. До побачення!")
            break
            
        else:
            # обробка невірного вводу
            print("Помилка: Неправильний вибір. Введіть число від 1 до 6.")

if __name__ == "__main__":
    main()

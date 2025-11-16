import json
import os
from typing import List, Dict, Any

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_FILE = os.path.join(SCRIPT_DIR, "teams_db.json")
RESULT_FILE = os.path.join(SCRIPT_DIR, "team_analysis_result.json")

TeamData = List[Dict[str, Any]]

def get_default_data() -> TeamData:
    return [
        {"name": "Сонечки", "points": 85},
        {"name": "Квіточки", "points": 80},
        {"name": "Бджілочки", "points": 77},
        {"name": "Хвильки", "points": 75},
        {"name": "Млинчики", "points": 68},
        {"name": "Котики", "points": 65},
        {"name": "Слони", "points": 60},
        {"name": "Літачки", "points": 51},
        {"name": "Промінчики", "points": 40}
    ]

def load_data(filename: str) -> TeamData:
    if not os.path.exists(filename):
        print(f"Файл {filename} не знайдено. Створюю новий...")
        default_data = get_default_data()
        save_data(filename, default_data)
        return default_data
        
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
            if not isinstance(data, list):
                print(f"Помилка: {filename} має невірний формат (не список).")
                return []
            return data
    except json.JSONDecodeError:
        print(f"Помилка: Не вдалося прочитати {filename}. Файл пошкоджено.")
        return []
    except Exception as e:
        print(f"Виникла неочікувана помилка при читанні {filename}: {e}")
        return []

def save_data(filename: str, data: Any) -> None:
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"Помилка: Не вдалося зберегти дані у файл {filename}.")
        print(f"Деталі помилки: {e}")

def display_all_teams(filename: str) -> None:
    print("\n--- 1. Список всіх команд ---")
    data = load_data(filename)
    if not data:
        print("База даних команд порожня.")
        return

    data.sort(key=lambda team: team['points'], reverse=True)
    
    place = 1
    for team in data:
        print(f"  {place}. Команда: {team.get('name', 'N/A')}, Очки: {team.get('points', 'N/A')}")
        place += 1

def add_team(filename: str) -> None:
    print("\n--- 2. Додавання нової команди ---")
    data = load_data(filename)
    existing_names = [team['name'].lower() for team in data]

    while True:
        team_name = input("Введіть назву нової команди: ").strip()
        if not team_name:
            print("Помилка: Назва команди не може бути порожньою.")
        elif team_name.lower() in existing_names:
            print(f"Помилка: Команда з назвою '{team_name}' вже є у базі.")
        else:
            break
            
    while True:
        points_str = input(f"Введіть кількість очок для '{team_name}': ").strip()
        if not points_str.isdigit():
            print("Помилка: Кількість очок має бути додатним цілим числом.")
            continue
        
        points = int(points_str)
        if points < 0:
            print("Помилка: Кількість очок не може бути від'ємною.")
        else:
            break
            
    new_team = {"name": team_name, "points": points}
    data.append(new_team)
    save_data(filename, data)
    print(f"Команду '{team_name}' з {points} очками успішно додано.")

def delete_team(filename: str) -> None:
    print("\n--- 3. Видалення команди ---")
    data = load_data(filename)
    if not data:
        print("База даних порожня. Нема чого видаляти.")
        return

    team_name = input("Введіть точну назву команди, яку хочете видалити: ").strip()
    if not team_name:
        print("Помилка: Назва команди не може бути порожньою.")
        return

    team_to_delete = None
    for team in data:
        if team.get('name', '').lower() == team_name.lower():
            team_to_delete = team
            break

    if team_to_delete:
        print(f"Ви впевнені, що хочете видалити команду: {team_to_delete['name']} (Очки: {team_to_delete['points']})?")
        confirmation = input("Введіть 'так' для підтвердження: ").strip().lower()

        if confirmation == 'так':
            data.remove(team_to_delete)
            save_data(filename, data)
            print(f"Команду '{team_to_delete['name']}' успішно видалено.")
        else:
            print("Видалення скасовано.")
    else:
        print(f"Помилка: Команди з назвою '{team_name}' не знайдено в базі.")

def find_team(filename: str) -> None:
    print("\n--- 4. Пошук команди за назвою ---")
    data = load_data(filename)
    if not data:
        print("База даних порожня.")
        return

    team_name = input("Введіть назву команди для пошуку: ").strip()
    
    found = False
    for team in data:
        if team.get('name', '').lower() == team_name.lower():
            print("\nЗнайдено команду:")
            print(f"  Назва: {team['name']}")
            print(f"  Очки: {team['points']}")
            found = True
            break
            
    if not found:
        print(f"Команду з назвою '{team_name}' не знайдено.")

def analyze_tenth_team(db_filename: str, result_filename: str) -> None:
    print("\n--- 5. Аналіз місця 10-ї команди ---")
    data = load_data(db_filename)
    
    if not data:
        print("Помилка: База даних команд порожня. Неможливо провести аналіз.")
        return

    try:
        all_points = [team['points'] for team in data]
        max_points = max(all_points)
        min_points = min(all_points)
    except ValueError:
        print("Помилка: Неможливо визначити min/max очок (можливо, база порожня).")
        return

    while True:
        new_name = input("Введіть назву нової 10-ї команди: ").strip()
        if not new_name:
            print("Помилка: Назва команди не може бути порожньою.")
        else:
            break
            
    while True:
        points_str = input(f"Введіть кількість очок для '{new_name}': ").strip()
        
        if not points_str.isdigit():
            print("Помилка: Кількість очок має бути додатним цілим числом.")
            continue
            
        new_points = int(points_str)
        
        if new_points >= max_points:
            print(f"Помилка: Команда не може стати чемпіоном (мати {new_points} >= {max_points} очок).")
        elif new_points <= min_points:
            print(f"Помилка: Команда не може зайняти останнє місце (мати {new_points} <= {min_points} очок).")
        else:
            break

    place = 1
    for team in data:
        if team['points'] > new_points:
            place += 1
            
    teams_below = []
    for team in data:
        if team['points'] < new_points:
            teams_below.append(team['name'])
            
    print(f"\nРезультат аналізу для '{new_name}' ({new_points} очок):")
    print(f"  а) Місце, яке зайняла команда: {place}")
    if not teams_below:
        print("  б) Немає команд, які набрали менше очок.")
    else:
        print(f"  б) Команди, які набрали менше очок: {', '.join(teams_below)}")

    result_data = {
        "analyzed_team_name": new_name,
        "analyzed_team_points": new_points,
        "calculated_place": place,
        "teams_with_fewer_points": teams_below
    }
    
    save_data(result_filename, result_data)
    print(f"Результат аналізу успішно збережено у файл: {result_filename}")

def print_menu() -> None:
    print("\n--- Меню ---")
    print(" 1. Вивести повний список команд")
    print(" 2. Додати нову команду до бази")
    print(" 3. Видалити команду з бази")
    print(" 4. Знайти команду за назвою")
    print(" 5. Проаналізувати місце 10-ї команди (Варіант 1)")
    print(" 6. Вийти з програми")

def main() -> None:    
    load_data(DATA_FILE) 
    
    while True:
        print_menu()
        choice = input("Введіть ваш вибір (1-6): ").strip()
        
        if choice == '1':
            display_all_teams(DATA_FILE)
        
        elif choice == '2':
            add_team(DATA_FILE)
            
        elif choice == '3':
            delete_team(DATA_FILE)
            
        elif choice == '4':
            find_team(DATA_FILE)
            
        elif choice == '5':
            analyze_tenth_team(DATA_FILE, RESULT_FILE)
            
        elif choice == '6':
            print("Завершення роботи програми. До побачення!")
            break
            
        else:
            print("Помилка: Неправильний вибір. Введіть число від 1 до 6.")

if __name__ == "__main__":
    main()

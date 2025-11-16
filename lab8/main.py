import os

DIR = os.path.dirname(os.path.abspath(__file__))
FILE_NAME = os.path.join(DIR, "lab8.txt")

### частина коду Данила ###

def task_danylo(filename: str) -> None:
    # створює або перезаписує файл, додаючи питання від першого учасника
    print(f"\n--- Завдання 1: Данило ---")
    
    content = (
        "--- Учасник 1: Данило ---\n"
        # питання
        "Питання: Яка ключова різниця між режимами 'w' та 'a' при відкритті файлу?\n\n"
    )
    
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Файл '{filename}' успішно створено/перезаписано з питанням.")
        
    except IOError as e:
        print(f"Помилка: Не вдалося записати у файл '{filename}'.")
        print(f"Деталі: {e}")
    except Exception as e:
        print(f"Виникла неочікувана помилка: {e}")

### кінець частини коду Данила ###



### частина коду Данила ###

def read_file_content(filename: str) -> None:
    # читає та виводить вміст текстового файлу
    print(f"\n--- Вміст файлу '{filename}' ---")
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            if not content:
                print("(Файл порожній)")
            else:
                print(content.strip())
                
    except FileNotFoundError:
        print(f"Помилка: Файл '{filename}' ще не створено.")
        print("Спочатку потрібно виконати завдання 1.")
    except IOError as e:
        print(f"Помилка: Не вдалося прочитати файл. Деталі: {e}")
    print("--- Кінець файлу ---")


def print_menu() -> None:
    # виводить головне меню програми
    print("\n--- Головне Меню ---")
    print("Оберіть дію:")
    print("1. Завдання 1 (Данило: Створити файл та поставити питання)")
    print("2. Прочитати вміст файлу")
    print("3. Вийти з програми")


def main() -> None:
    # головна функція, що керує роботою програми
    while True:
        print_menu()
        choice = input("Введіть ваш вибір (1-3): ").strip()
        
        if choice == '1':
            task_danylo(FILE_NAME)
        
        elif choice == '2':
            read_file_content(FILE_NAME)
            
        elif choice == '3':
            print("Завершення роботи програми. До побачення!")
            break
            
        else:
            print("Помилка: Неправильний вибір. Введіть число від 1 до 3.")


if __name__ == "__main__":
    main()

### кінець частини коду Данила ###

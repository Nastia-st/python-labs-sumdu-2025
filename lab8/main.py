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
### частина коду Софії ###

def task_sofia(filename: str) -> None:
    # додає відповідь на перше питання та ставить нове питання
    print(f"\n--- Завдання 2: Софія ---")
    
    content = (
        "--- Учасник 2: Софія ---\n"
        "Відповідь: Режим 'w' (write) повністю перезаписує файл (або створює новий), "
        "видаляючи весь попередній вміст. Режим 'a' (append) додає нові дані "
        "в кінець файлу, не чіпаючи те, що вже було записано.\n"
        # питання
        "Питання: Для чого використовується конструкція 'if __name__ == \"__main__\":' в Python?\n\n"
    )
    
    try:
        with open(filename, 'a', encoding='utf-8') as f:
            f.write(content)
        print(f"Відповідь та нове питання успішно додано до '{filename}'.")
        
    except FileNotFoundError:
        print(f"Помилка: Файл '{filename}' не знайдено.")
        print("Спочатку потрібно виконати завдання 1.")
    except IOError as e:
        print(f"Помилка: Не вдалося записати у файл '{filename}'. Деталі: {e}")

### кінець частини коду Софії ###

### частина коду Микити ###

def task_mykyta(filename: str) -> None:
    # додає відповідь на друге питання та ставить третє питання
    print(f"\n--- Завдання 3: Микита ---")
    
    content = (
        "--- Учасник 3: Микита ---\n"
        "Відповідь: Ця конструкція дозволяє виконувати певний блок коду "
        "тільки тоді, коли файл запускається як головна програма (скрипт), "
        "а не коли він імпортується як модуль в інший файл.\n"
        # питання
        "Питання: Поясніть базовий принцип роботи алгоритму 'Швидкого сортування' (Quicksort)?\n\n"
    )
    
    try:
        with open(filename, 'a', encoding='utf-8') as f:
            f.write(content)
        print(f"Відповідь та нове питання успішно додано до '{filename}'.")

    except FileNotFoundError:
        print(f"Помилка: Файл '{filename}' не знайдено.")
        print("Спочатку потрібно виконати завдання 1 та 2.")
    except IOError as e:
        print(f"Помилка: Не вдалося записати у файл '{filename}'. Деталі: {e}")

### кінець частини коду Микити ###
### частина коду Анастасії ###

def task_nastia(filename: str) -> None:
    # додає фінальну відповідь на третє питання
    print(f"\n--- Завдання 4: Анастасія ---")
    
    content = (
        "--- Учасник 4: Анастасія ---\n"
        "Відповідь: Швидке сортування (Quicksort) - це рекурсивний алгоритм."
        "Він працює так: 1) Обирається опорний елемент (pivot) зі списку."
        "2) Список ділиться на два під-списки: елементи, менші за опорний,"
        "та елементи, більші за опорний. 3) Кроки 1-2 рекурсивно"
        "повторюються для під-списків, доки вони не будуть відсортовані.\n\n"
    )
    
    try:
        with open(filename, 'a', encoding='utf-8') as f:
            f.write(content)
        print(f"Фінальну відповідь успішно додано до '{filename}'.")

    except FileNotFoundError:
        print(f"Помилка: Файл '{filename}' не знайдено.")
        print("Спочатку потрібно виконати завдання 1, 2 та 3.")
    except IOError as e:
        print(f"Помилка: Не вдалося записати у файл '{filename}'. Деталі: {e}")

### кінець частини коду Анастасії ###
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
    print("2. Завдання 2 (Софія: Відповісти та поставити питання)")
    print("3. Завдання 3 (Микита: Відповісти та поставити питання)")
    print("4. Завдання 4 (Анастасія: Надати фінальну відповідь)")
    print("5. Прочитати вміст файлу")
    print("6. Вийти з програми")


def main() -> None:
    # головна функція, що керує роботою програми
    while True:
        print_menu()
        choice = input("Введіть ваш вибір (1-6): ").strip()
        
        if choice == '1':
            task_danylo(FILE_NAME)

        elif choice == '2':
            task_sofia(FILE_NAME)

        elif choice == '3':
            task_mykyta(FILE_NAME)

        elif choice == '4':
            task_nastia(FILE_NAME)
            
        elif choice == '5':
            read_file_content(FILE_NAME)
            
        elif choice == '6':
            print("Завершення роботи програми. До побачення!")
            break
            
        else:
            print("Помилка: Неправильний вибір. Введіть число від 1 до 6.")


if __name__ == "__main__":
    main()

### кінець частини коду Данила ###

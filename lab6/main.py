### частина коду Данила ###

# словник для зберігання інформації про студентів
students_db = {
    "Петренко Петро Петрович": {
        "group": "КН-43",
        "course": 2,
        "subjects": {
            "Програмування мовою Python": 95,
            "Чисельні методи": 88,
            "Англійська мова": 92
        }
    },
    "Іванова Марія Іванівна": {
        "group": "КН-44",
        "course": 2,
        "subjects": {
            "Програмування мовою Python": 100,
            "Англійська мова": 90,
            "Алгоритми та структури даних": 94
        }
    }
}

def add_student(db: dict) -> None:
    # додає нового студента до словника
    print("\n--- Додавання нового студента ---")
    
    # 1. введення ПІБ
    while True:
        full_name = input("Введіть ПІБ студента (Прізвище Ім'я По батькові): ").strip()
        if not full_name:
            print("Помилка: ПІБ не може бути порожнім.")
        elif full_name in db:
            print(f"Помилка: Студент з ПІБ '{full_name}' вже є у базі.")
        else:
            break
            
    # 2. введення групи
    while True:
        group = input(f"Введіть номер групи для '{full_name}': ").strip()
        if not group:
            print("Помилка: Номер групи не може бути порожнім.")
        else:
            break

    # 3. введення курсу
    course = 0
    while True:
        course_str = input(f"Введіть курс (наприклад, 1): ").strip()
        if not course_str.isdigit():
            print("Помилка: Введіть додатне ціле число для курсу.")
            continue
            
        course = int(course_str)
        if course <= 0 or course > 6:
            print("Помилка: Курс має бути в діапазоні від 1 до 6.")
        else:
            break

    # 4. введення предметів та оцінок
    print("\nВведіть предмети та оцінки (0-100).")
    print("Залиште назву предмету порожньою, щоб завершити.")
    subjects = {}
    while True:
        subject_name = input("Введіть назву предмету: ").strip()
        if not subject_name:
            break # завершення введення предметів
            
        grade = -1
        while True:
            grade_str = input(f"Введіть оцінку з предмету '{subject_name}': ").strip()
            if not grade_str.isdigit():
                print("Помилка: Оцінка має бути цілим числом.")
                continue
                
            grade = int(grade_str)
            if not (0 <= grade <= 100):
                print("Помилка: Оцінка має бути в діапазоні від 0 до 100.")
            else:
                break
                
        subjects[subject_name] = grade

    # 5. додавання до словника
    db[full_name] = {
        "group": group,
        "course": course,
        "subjects": subjects
    }
    print(f"\nСтудента '{full_name}' успішно додано до бази.")

def display_all_students(db: dict):
    # виводить інформацію про всіх студентів у словнику
    print("\n--- Список всіх студентів ---")
    if not db:
        print("База даних студентів порожня.")
        return

    count = 1
    for full_name, info in db.items():
        print(f"\n{count}. ПІБ: {full_name}")
        print(f"   Група: {info['group']}")
        print(f"   Курс: {info['course']}")
        print("   Предмети та оцінки:")
        if not info['subjects']:
            print("     (немає)")
        else:
            for subject, grade in info['subjects'].items():
                print(f"     - {subject}: {grade}")
        count += 1

### кінець частини коду Данила ###
### частина коду Софії ###

def find_student(db: dict):
    # шукає студента за ПІБ та виводить детальну інформацію
    print("\n--- Пошук студента ---")
    name_to_find = input("Введіть точне ПІБ студента для пошуку: ").strip()
    
    if name_to_find in db:
        info = db[name_to_find]
        print(f"\nЗнайдено студента: {name_to_find}")
        print(f"  Група: {info['group']}")
        print(f"  Курс: {info['course']}")
        print("  Предмети та оцінки:")
        if not info['subjects']:
            print("    (немає)")
        else:
            for subject, grade in info['subjects'].items():
                print(f"    - {subject}: {grade}")
    else:
        print(f"Студента з ПІБ '{name_to_find}' не знайдено.")

### кінець частини коду Софії ###
### частина коду Микити ###

def edit_student_info(db: dict) -> None:
    # надає меню для редагування інформації про існуючого студента
    print("\n--- Редагування даних студента ---")
    name_to_edit = input("Введіть ПІБ студента, дані якого хочете змінити: ").strip()

    if name_to_edit not in db:
        print(f"Помилка: Студента '{name_to_edit}' не знайдено.")
        return

    student = db[name_to_edit]
    print(f"Обрано студента: {name_to_edit}")

    while True:
        print("\nЩо ви хочете змінити?")
        print("1. Змінити групу")
        print("2. Змінити курс")
        print("3. Змінити оцінку з предмету")
        print("4. Повернутися до головного меню")
        choice = input("Ваш вибір (1-4): ").strip()

        if choice == '1':
            # зміна групи
            new_group = input(f"Введіть нову групу (поточна: {student['group']}): ").strip()
            if new_group:
                student['group'] = new_group
                print(f"Групу оновлено на '{new_group}'.")
            else:
                print("Ввід скасовано, група не змінилась.")
        
        elif choice == '2':
            # зміна курсу
            try:
                new_course_str = input(f"Введіть новий курс (поточний: {student['course']}): ").strip()
                new_course = int(new_course_str)
                if 1 <= new_course <= 6:
                    student['course'] = new_course
                    print(f"Курс оновлено на {new_course}.")
                else:
                    print("Помилка: Курс має бути від 1 до 6.")
            except ValueError:
                print("Помилка: Введіть коректне число.")
        
        elif choice == '3':
            # зміна оцінки
            print("Поточні предмети та оцінки:")
            if not student['subjects']:
                print("  (предметів немає)")
                continue
            
            for subj, grad in student['subjects'].items():
                print(f"  - {subj}: {grad}")
            
            subject_to_edit = input("Введіть назву предмету, оцінку з якого хочете змінити: ").strip()
            
            if subject_to_edit not in student['subjects']:
                print(f"Помилка: Предмет '{subject_to_edit}' не знайдено у цього студента.")
            else:
                try:
                    new_grade_str = input(f"Введіть нову оцінку (0-100) для '{subject_to_edit}': ").strip()
                    new_grade = int(new_grade_str)
                    if 0 <= new_grade <= 100:
                        student['subjects'][subject_to_edit] = new_grade
                        print("Оцінку успішно оновлено.")
                    else:
                        print("Помилка: Оцінка має бути від 0 до 100.")
                except ValueError:
                    print("Помилка: Введіть коректне число.")

        elif choice == '4':
            print(f"Завершено редагування для {name_to_edit}.")
            break
        
        else:
            print("Помилка: Невірний вибір. Введіть число від 1 до 4.")

### кінець частини коду Микити ###
### частина коду Анастасії ###

def delete_student(db: dict):
    # видаляє студента з словника за ПІБ
    print("\n--- Видалення студента ---")
    name_to_delete = input("Введіть ПІБ студента, якого хочете видалити: ").strip()

    if name_to_delete not in db:
        print(f"Помилка: Студента '{name_to_delete}' не знайдено.")
        return

    # крок підтвердження
    print(f"Ви впевнені, що хочете назавжди видалити студента: {name_to_delete}?")
    confirmation = input("Введіть 'так' для підтвердження: ").strip().lower()

    if confirmation == 'так':
        del db[name_to_delete]
        print(f"Студента '{name_to_delete}' успішно видалено.")
    else:
        print("Видалення скасовано.")

### кінець частини коду Анастасії ###
### частина коду Данила ###

def print_menu() -> None:
    # виводить головне меню програми
    print("\n--- Головне Меню ---")
    print("1. Додати нового студента")
    print("2. Показати список всіх студентів")
    print("3. Знайти студента за ПІБ")
    print("4. Редагувати дані студента")
    print("5. Видалити студента")
    print("6. Вийти з програми")
    
def main() -> None:
    # головна функція, що керує роботою програми
    while True:
        print_menu()
        choice = input("Введіть ваш вибір (1-6): ").strip()
        
        if choice == '1':
            add_student(students_db)
        
        elif choice == '2':
            display_all_students(students_db)
            
        elif choice == '3':
            find_student(students_db)

        elif choice == '4':
            edit_student_info(students_db)

        elif choice == '5':
            delete_student(students_db)
            
        elif choice == '6':
            print("Завершення роботи програми. До побачення!")
            break
            
        else:
            print("Помилка: Неправильний вибір. Введіть число від 1 до 6.")

if __name__ == "__main__":
    main()

### кінець частини коду Данила ###

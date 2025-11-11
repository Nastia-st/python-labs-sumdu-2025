import string
import os

DIR = os.path.dirname(os.path.abspath(__file__))
FILE_1 = os.path.join(DIR, "TF1_1.txt")
FILE_2 = os.path.join(DIR, "TF1_2.txt")

def create_tf1_1(filename: str) -> None:
    # вміст першого файлу
    content = [
        "перший рядок, з комою і крапкою ->.",
        "другий: має двокрапку; крапку з комою, і оцього прикола ☺.",
        "хоба третій! просто рядок!",
        "четвертий... з крапками та іншими усякими знаками -+/*."
    ]
    
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            for line in content:
                f.write(line + "\n")
        print(f"Файл '{filename}' успішно створено та записано.")
    except Exception as e:
        print(f"Помилка: Не вдалося створити або записати у файл '{filename}'.")
        print(f"Деталі помилки: {e}")

def process_to_tf1_2(source_file: str, dest_file: str) -> None:
    translator = str.maketrans(string.punctuation, ' ' * len(string.punctuation))
    
    try:
        with open(source_file, 'r', encoding='utf-8') as f_in, open(dest_file, 'w', encoding='utf-8') as f_out:
            word_count = 0
            for line in f_in:
                cleaned_line = line.translate(translator)
                words = cleaned_line.split()

                for word in words:
                    f_out.write(word + "\n")
                    word_count += 1
        
            print(f"Файл '{dest_file}' успішно створено.")
            print(f"Успішно оброблено та записано слів: {word_count}")

    except FileNotFoundError:
        print(f"Помилка: Файл-джерело '{source_file}' не знайдено.")
    except Exception as e:
        print(f"Помилка під час читання/запису файлу: {e}")

def print_tf1_2(filename: str) -> None:
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            
            if not lines:
                print("(Файл порожній)")
                return
                        
            print("Вміст файлу:")
            for line in lines:
                print(line.strip())
            
    except FileNotFoundError:
        print(f"Помилка: Файл '{filename}' не знайдено для читання.")
    except Exception as e:
        print(f"Помилка під час читання файлу: {e}")

def main() -> None:
    # а) створює текстовий файл TF1_1 із символьних рядків різної довжини, слова в яких розділені пробілами і розділовими знаками
    print(f"\n--- Завдання А • Створення файлу {FILE_1} ---")
    create_tf1_1(FILE_1)

    # б) читає вміст файла TF1_1 і записує кожне слово в окремий рядок файла TF1_2 (розділові знаки опускаються)
    print(f"\n--- Завдання Б • Обробка {FILE_1} -> {FILE_2} ---")
    process_to_tf1_2(FILE_1, FILE_2)
    
    # в) читає вміст файла TF1_2 і друкує його по рядках
    print(f"\n--- Завдання В • Друк вмісту файлу {FILE_2} ---")
    print_tf1_2(FILE_2)

if __name__ == "__main__":
    main()

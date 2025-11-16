import csv
import os
import sys

DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_FILENAME = os.path.join(DIR, "lab9.csv")
OUTPUT_FILENAME = os.path.join(DIR, "result.csv")

data_from_file = [] 

print(f"--- Вміст .csv файлу {INPUT_FILENAME} ---")
try:
    with open(INPUT_FILENAME, mode='r', encoding='utf-8') as csvfile:
        
        reader = csv.DictReader(csvfile)
        
        print(f"{'Country Name':<45} | 2019 [YR2019]")
        print("-" * 70)
        
        for row in reader:
            gdp_value = row.get('2019 [YR2019]', 'N/A') 
            
            print(f"{row.get('Country Name', 'N/A'):<45} | {gdp_value}")
            
            data_from_file.append(row)

except FileNotFoundError:
    print(f"\nПомилка: Файл '{INPUT_FILENAME}' не знайдено.")
    print("Будь ласка, переконайся, що файл лежить в тій самій папці, що і скрипт.")
    sys.exit()
except Exception as e:
    print(f"\nПомилка при читанні файлу: {e}")
    sys.exit()

print("-" * 70)
print(f"Прочитано {len(data_from_file)} рядків.\n")

print("--- Початок пошуку країн ---")
print("Вводьте назви країн по одній. Для завершення введіть 'стоп'.\n")

countries_found_count = 0

try:
    with open(OUTPUT_FILENAME, mode='w', newline='', encoding='utf-8') as csvfile2:
        
        writer = csv.writer(csvfile2)
        
        writer.writerow(['Country Name', '2019 [YR2019]'])
        
        while True:
            search_country = input("Введіть назву країни (або 'стоп' для виходу): ")
            
            if search_country.strip().lower() == 'стоп':
                print("\nЗавершуємо пошук...")
                break
            
            flag_this_country_found = False
            
            for row in data_from_file:
                if row['Country Name'].strip().lower() == search_country.strip().lower():
                    
                    gdp_value = row.get('2019 [YR2019]', 'N/A')
                    
                    if gdp_value and gdp_value != '..':
                        print(f"  -> Знайдено: {row['Country Name']}, ВВП: {gdp_value}")
                        
                        writer.writerow([row['Country Name'], gdp_value])
                        
                        countries_found_count += 1
                        flag_this_country_found = True
                        
                        break 
            
            if not flag_this_country_found:
                print(f"  -> '{search_country}' не знайдено (перевірте написання).")

except Exception as e:
    print(f"\nПомилка під час пошуку або запису: {e}")
    sys.exit()

print("\n--- Пошук завершено ---")
if countries_found_count > 0:
    print(f"Успішно знайдено та збережено {countries_found_count} країн.")
    print(f"Всі результати у файлі: '{OUTPUT_FILENAME}'")
else:
    print("Не було знайдено та збережено жодної країни.")

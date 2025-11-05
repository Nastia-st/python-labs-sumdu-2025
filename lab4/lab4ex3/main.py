def insert_element():
    
    A_str = input("Введіть список (елементи через пробіл): ")
    A = A_str.split()

    while not A:
        print("Список не може бути порожнім.")
        A_str = input("Введіть список (елементи через пробіл): ")
        A = A_str.split()
        
    print("Оригінальний список:", A)

    k_str = input(f"Введіть індекс елементу (від 0 до {len(A) - 1}), ПІСЛЯ якого вставити новий елемент: ")

    while not k_str.isdigit() or not (0 <= int(k_str) < len(A)):
        print(f"Помилка: індекс має бути числом від 0 до {len(A) - 1}.")
        k_str = input(f"Введіть коректний індекс (від 0 до {len(A) - 1}): ")
    
    k = int(k_str)
    
    new_element = input("Введіть новий елемент, який треба вставити: ")

    result = []
    for i in range(len(A)):
        result.append(A[i])
        if i == k:
            result.append(new_element)

    print("Оновлений список:", result)
    return result

insert_element()

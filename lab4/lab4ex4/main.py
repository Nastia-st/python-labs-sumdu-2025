def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        
        left = []
        middle = []
        right = []
        
        for x in arr:
            if x < pivot:
                left.append(x)
            elif x == pivot:
                middle.append(x)
            else:
                right.append(x)
        
        return quicksort(left) + middle + quicksort(right)

def run_quicksort_task():
    
    # 1. отримання списку
    A_str = input("Введіть список (числа через пробіл): ")
    A_parts = A_str.split()

    # 2. валідація
    valid = False
    while not valid:
        # перевірка на порожній список
        if not A_parts:
            print("Список не може бути порожнім.")
            A_str = input("Введіть список (числа через пробіл): ")
            A_parts = A_str.split()
            continue

        # перевірка, що всі елементи - числа
        all_digits = True
        for part in A_parts:
            # перевірка на ціле число
            if not (part.isdigit() or (part.startswith('-') and part[1:].isdigit())):
                all_digits = False
                break
        
        if all_digits:
            valid = True
        else:
            print("Помилка: введіть тільки цілі числа, розділені пробілом.")
            A_str = input("Введіть список (числа через пробіл): ")
            A_parts = A_str.split()

    # 3. конвертація в int
    A = [int(part) for part in A_parts]
    
    print("Оригінальний список:", A)
    
    # 4. виклик сортування
    sorted_A = quicksort(A)
    
    # 5. вивід результату
    print("Відсортований список (Швидким сортуванням):", sorted_A)
    
    # 6. повернення результату
    return sorted_A

run_quicksort_task()

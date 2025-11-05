def find_fib_in_set():

    numbers_set = set(range(1, 51))
    
    fib_set = set()
    a, b = 0, 1
    while a <= 50:
        fib_set.add(a)
        a, b = b, a + b

    common_fibs = numbers_set.intersection(fib_set)
    
    print(f"Множина 1 (Числа від 1 до 50): {numbers_set}")
    print(f"Множина 2 (Числа Фібоначчі <= 50): {fib_set}")
    print(f"Перетин (Числа Фібоначчі від 1 до 50): {common_fibs}")
    
    count = len(common_fibs)
    print(f"\nКількість чисел Фібоначчі у множині від 1 до 50: {count}")
    
    return count

find_fib_in_set()

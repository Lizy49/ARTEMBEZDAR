def print_even_numbers(arr):
    even_numbers = []
    
    
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] % 2 == 0:
            even_numbers.append(arr[i])


    K = len(even_numbers)
    print(f'Четные числа: {even_numbers}')
    print(f'Количество четных чисел K: {K}')


N = int(input("Введите размер списка: "))
numbers = []


for _ in range(N):
    num = int(input("Введите число: "))
    numbers.append(num)


print_even_numbers(numbers)

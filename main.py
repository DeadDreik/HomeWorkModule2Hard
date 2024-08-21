def numbers(rand_number):
    pairs_numb = []
    for i in range(1, rand_number):
        j = i + 1
        for j in range(i + 1, rand_number + 1):
            if rand_number % (i + j) == 0:
                if rand_number % (i + j) == 0:
                    pairs_numb.append((i, j))
                return pairs_numb
first_number = int(input('Введите число:'))
if 3 <= first_number <= 20:
    result_pairs = numbers(first_number)
    # Объединяем пары в строку для вывода
    password = ''.join([f"{i}{j}" for i, j in result_pairs])
    print(f'Для числа {first_number} подходят пароли: {password}')
else:
    print("Число вне допустимого диапазона.")

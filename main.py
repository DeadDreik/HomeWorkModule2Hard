def numbers(rand_number):
    pairs_numb = list()
    limit_first_numb = (rand_number + 1) // 2
    for i in range(1, limit_first_numb):
        j = i + 1
        while i + j <= rand_number:
            if rand_number % (i + j) == 0:
                tuple_numbers = (i, j)
                pairs_numb.append(tuple_numbers)
            j += 1
    return pairs_numb
first_number = int(input('Введите число:'))
print('Для числа', first_number, 'подходят пароли:', numbers(first_number))

# Задание 1. Удаление дубликатов из списка
# Дан список повторяющихся элементов. Вернуть список с дублирующимися
# элементами. В результирующем списке не должно быть дубликатов.

# elements = [1, 2, 2, 3, 4, 4, 4, 5, 5]
# # Создаем пустой список для дублирующихся элементов
# duplicates = []
# # Проходим по каждому элементу в списке
# for x in elements:
#     if elements.count(x) > 1 and x not in duplicates:
#         duplicates.append(x)
# print(duplicates)

# Задача 2. Поиск наибольшего числа в списке
# Напишите программу, которая принимает список чисел через строку и
# возвращает наибольшее число в этом списке.


# Преобразуем каждую часть в целое число и создаем список чисел
# numbers = [int(x) for x in input("Введите числа через пробел:").split()]
#
# max_number = numbers[0]
# # Проходим по каждому числу в списке
# for num in numbers:
#
#     if num > max_number:
#         max_number = num
# print(max_number)


# Задача 3. Проверка палиндрома
# Напишите программу, которая принимает строку и определяет, является ли она
# палиндромом (читается одинаково с обеих сторон).

string = input("Введите строку: ").lower()
# Создаем множество для символов с нечетным количеством вхождений
odd_chars = set()

for char in string:

    if char in odd_chars:
        odd_chars.remove(char)

    else:
        odd_chars.add(char)

if len(odd_chars) <= 1:
    print("Строка является палиндромом")
else:
    print("Строка не является палиндромом")

# Задача 4. Генерация паролей
# Напишите программу, которая генерирует случайный пароль заданной длины,
# состоящий из букв, цифр и специальных символов.

# import random
#
# import string
#
# length = int(input("Введите длину пароля: "))
#
# characters = string.ascii_letters + string.digits + string.punctuation
#
# password = ''.join(random.choice(characters) for i in range(length))
# # Выводим сгенерированный пароль
# print(password)


# Задача 5. Нахождение анаграмм
# Напишите программу, которая принимает два слова и определяет, являются ли
# они анаграммами.

word1 = input("Введите первое слово: ")
word2 = input("Введите второе слово: ")

if len(word1) != len(word2):
    print("Слова не являются анаграммами")
else:

    char_count1 = {}
    char_count2 = {}

    for char in word1:
        if char in char_count1:
            char_count1[char] += 1
        else:
             char_count1[char] = 1

    for char in word2:
        if char in char_count2:
            char_count2[char] += 1
        else:
            char_count2[char] = 1

    if char_count1 == char_count2:
        print("Слова являются анаграммами")
    else:
        print("Слова не являются анаграммами")

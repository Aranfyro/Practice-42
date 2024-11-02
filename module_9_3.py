# Домашнее задание по теме "Генераторные сборки"

first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(x) - len(y) for x,y in zip(first, second) if len(x) != len(y))
second_result = (len(first[x]) == len(second[x]) for x in range(0, 3))

print(list(first_result))
print(list(second_result))
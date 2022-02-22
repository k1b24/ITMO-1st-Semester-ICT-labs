#335106 % 4 = 2
import re

#описываем функцию для замены найденного числа
def replace_function(string_number):
    x = int(string_number)
    return str(3 * x**2 + 5)

#создаем функцию шифровки
def encrypt_message(filename):
    file_to_check = open(filename,'r', encoding='utf-8-sig')
    file_to_strings = []
    pattern = re.compile('[0-9]+')#создаем паттерн поиска числа
    #заполняем массив fileToStrings строками из файла
    for string in file_to_check:
        file_to_strings.append(string.rstrip())
    #проходимся по массиву строк из файла и с помощью регулярного выражения находим все числа и заменяем их при помощи функции
    for i in range(len(file_to_strings)):
        numbers_in_string = re.findall(pattern, file_to_strings[i])
        for number in numbers_in_string:
            file_to_strings[i] = file_to_strings[i].replace(number, replace_function(number))
    #выводим строки на экран
    for string in file_to_strings:
        print(string)
        
#Запускам пять тестов для проверки написанной функциий
for i in range(1,6):
    print('-----New Test-----')
    current_test = 'test' + str(i) + '.txt'
    encrypt_message(current_test)
    
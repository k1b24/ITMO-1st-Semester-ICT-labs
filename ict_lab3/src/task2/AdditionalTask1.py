import re
#335106 % 6 = 0

#Создаем функцию для проверки файла на хайку
def check_if_haiku (filename):
    file_to_check = open(filename,'r', encoding='utf-8-sig')
    array_of_haiku_strings = file_to_check.read().split('/')
    pattern = re.compile('а|о|э|е|и|ы|у|ё|ю|я|А|О|Э|Е|И|Ы|У|Ё|Ю|Я')
    #Проверяем является ли хайку, для этого сначала проверяем количество строк в массиве ?= 3
    if len(array_of_haiku_strings) != 3:
        return('Не хайку. Должно быть 3 строки.')
    else: #иначе химичим :)
        check_3_strings = 0
        for i in range(3):
            if (len(re.findall(pattern, array_of_haiku_strings[i])) == 5) and (i == 0 or i == 2):
                check_3_strings += 1
            elif (len(re.findall(pattern, array_of_haiku_strings[i])) == 7) and (i == 1):
                check_3_strings += 1
        if check_3_strings == 3:
            return ('Хайку!')
        else:
            return ('Не хайку.')


#Запускам пять тестов для проверки написанной функциий
for i in range(1,6):
    current_test = 'test' + str(i) + '.txt'
    print(check_if_haiku(current_test))
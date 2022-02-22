import re
#ISU = 335106
# eyes = 1   nose = 2  mouth = 2

#создаем функцию проверки текста на смайлики
def check_for_smiles(filename):
    pattern = re.compile(r';-{O')
    file_to_check = open(filename)
    file_in_string = file_to_check.read()
    return len(pattern.findall(file_in_string))

#Запускам пять тестов для проверки написанной функциий
for i in range(1,6):
    current_test = 'test' + str(i) + '.txt'
    print(check_for_smiles(current_test))
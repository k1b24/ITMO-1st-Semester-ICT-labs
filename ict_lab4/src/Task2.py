def my_parse():
    import re
    # Функция для нахождения повторяющихся тегов, чтобы эти теги выносить в []
    def find_repitable_tags(m):
        repitable_tags = {} 
        for i in range(len(m)):
            tag_name = m[i][m[i].find('<')+1:m[i].find('>')].strip()
            if m.count(m[i]) != 1 and '</' not in m[i]:
                if tag_name not in repitable_tags:
                    repitable_tags[tag_name] = 1
                else:
                    repitable_tags[tag_name] += 1
        return repitable_tags


    #открываем xml файл
    xml_file = open('Schedule.xml', 'r', encoding='UTF-8')
    xml_lines = xml_file.readlines()
    xml_lines = xml_lines[1::]
    xml_string = ''
    for i in range(0, len(xml_lines)):
        xml_string += xml_lines[i].lstrip().rstrip()

    #создаем json файл
    json_file = open('Schedule.json', 'w', encoding='UTF-8')

    tabs = 0 #переменная отвечающая за отступы
    json_lines = ['{'] #массив в котором каждый элемент отвечает за каждую строку в финальном файле
    tabs += 1 
    repitable_tags = find_repitable_tags(xml_lines) # словарь отвечающий за повторяющиеся теги для установки []
    used_repitable_tags = [] #список хранящий в себе уже использованные в качестве открывающей [ теги 
    prev_is_content = False #переменная отвечающая за проверку предыдущей проходки по циклу, если в предыдущей проходке мы вычленяли контент, то она True, иначе False
    close_pattern = re.compile(r"<\/.+>$")# паттерн отвечающий за закрывающий тег
    open_pattern = re.compile(r"<[^\/]+>$")# паттерн отвечающий за открывающий тег

    while len(xml_string) != 0: #идем по строке с xml кодом и постепенно ее уменьшаем
        if bool(re.match(close_pattern, xml_string[:xml_string.find('>')+1])): #обработка строки если в ней встретился закрывающий тег
            nexttag = xml_string[3:]
            nexttag = nexttag[nexttag.find('<'):]
            nexttag = nexttag[:nexttag.find('>')+1] # находим следующий тег
            tabs -= 1
            if not(prev_is_content): # если предыдущая проходка не обрабатывала контент
                tag = xml_string[2:xml_string.find('>')] #текущий обрабатываемый тег
                if tag in repitable_tags and repitable_tags[tag] == 0 and nexttag != tag: #проверка тега на его принадлежность к повторяющемуся тегу
                    s = '  ' * tabs + '}\n'
                    tabs -= 1
                    s += '  ' * tabs + ']'
                    json_lines.append(s)
                else: 
                    json_lines.append('  ' * tabs + '}')
            if bool(re.match(open_pattern, nexttag)) and xml_string.count('>') > 1: #если следующий тег открывающийся
                json_lines[len(json_lines)-1] += ',' 
            prev_is_content = False     
            r = xml_string.find('>')
            xml_string = xml_string[r+1:]

        elif bool(re.match(open_pattern, xml_string[:xml_string.find('>')+1])): #обработка строки если в ней встретился открывающий тег
            r = xml_string.find('>')
            tag = xml_string[1:r]
            if tag not in repitable_tags: #если тег не повторяющийся
                s = '  ' * tabs + '"' + tag + '": '
                nexttag = xml_string[r+1:]
                nexttag = nexttag[:nexttag.find('>')+1]
                if bool(re.match(open_pattern, nexttag)): #является ли следующая строка тегом или нет
                    s += '{'
            elif tag not in used_repitable_tags: #иначе если тег повторяющийся и не использовалься
                s = '  ' * tabs + '"' + tag + '": [ \n'
                tabs += 1
                s += '  ' * tabs + '{'
                used_repitable_tags.append(tag)
                repitable_tags[tag] -= 1
            elif repitable_tags[tag] >= 1: #если использовался, но сейчас будет использоваться не в последний раз
                s = '  ' * tabs + '{'
                repitable_tags[tag] -= 1
            xml_string = xml_string [r+1:]
            tabs += 1
            json_lines.append(s)
            
        else: # #обработка строки во всех других случаях
            r = xml_string.find('<')
            content ='"' + xml_string[:r].strip() + '"'
            xml_string = xml_string[r:]
            json_lines[len(json_lines)-1] += content
            prev_is_content = True
        
    json_lines.append('}')
    for elem in json_lines:
        json_file.write(elem+'\n')

my_parse()
from xml.etree import ElementTree
import csv

# парсим xml
xml = ElementTree.parse("Schedule.xml")

# создаем csv файл
csvfile = open("Schedule.csv",'w', newline='', encoding='utf-8')
csvfile_writer = csv.writer(csvfile)

# добавляем заголовки в csv файл
csvfile_writer.writerow(["week","time","place", "room", "name", "teacher", "lesson-format"])

for schedule in xml.findall("schedule"):
    for day in schedule.findall("day"):
        for lessons in day.findall("lessons"):
            for lesson in lessons.findall("lesson"):
                if(lesson):
                    #извлечь данные о парах
                    week = lesson.find("week")
                    time = lesson.find("time")
                    place = lesson.find("place")
                    room = lesson.find("room")
                    name = lesson.find("name")
                    teacher = lesson.find("teacher")
                    lesson_format = lesson.find("lesson-format")
                    csv_line = [week.text.strip().replace(',', ';'), time.text.strip(), place.text.strip().replace(',', ';'), room.text.strip(), name.text.strip(), teacher.text.strip(), lesson_format.text.strip()]
                    
                    #добавить строку в файл
                    csvfile_writer.writerow(csv_line)
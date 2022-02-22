from Task2 import my_parse
from Task1 import parse_with_lib
import time

my_time = time.time()
for i in range(10):
    my_parse()
my_time = time.time() - my_time

libs_time = time.time()
for i in range(10):
    parse_with_lib()
libs_time = time.time() - libs_time


print('Парсер без готовых библиотек: ' + str(my_time))
print('Парсер с готовыми библиотеками: ' + str(libs_time))
if libs_time > my_time:
    print("Парсер без готовых библиотек быстрее.")
else: 
    print("Парсер с готовыми библиотеками быстрее.")
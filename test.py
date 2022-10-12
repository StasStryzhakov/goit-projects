from operator import index
import re
import string
import base64
import shutil
import os
import sys
import pathlib
from datetime import datetime
import random
from decimal import Decimal, getcontext
from collections import Counter
from collections import deque
from collections import namedtuple



names = ['Stas', 'Tanya', 'Mark', 'Vova', 'Olya', 'Luda', 'Pasha', 'Ivan', 'Andrey', 'Kostya', 'Nikita', 'Ira', 'Katya', 'Alena']
employees_list = [{random.sample(names, k=1)[0]: datetime(random.randint(1970, 2004), random.randint(1, 12), random.randint(1, 28))} for _ in range(100)]


def get_birthdays_per_week(employees_list: list):
    current_date = datetime.now()
    emploee_birthdays = {}
    week_day = ''
    for employee in employees_list:
        for name, birthday in employee.items():
            birthday_date_in_this_year = birthday.replace(year=current_date.year)
            if 1 <= (birthday_date_in_this_year - current_date).days <= 7:
                week_day = birthday.strftime('%A')
                emploee_birthdays.setdefault(week_day if week_day not in ('Sunday', 'Saturday') else 'Monday', []).append(name)
    
    for day, birthday_boy in emploee_birthdays.items():
        print(f'{day}: {", ".join(birthday_boy)}')





get_birthdays_per_week(employees_list)






# MAX_LEN = 5

# lifo = deque(maxlen=MAX_LEN)


# def push(element):
#     lifo.appendleft(element)


# def pop():
#     return lifo.popleft()

# def get_count_visits_from_ip(ips: list):
#     return Counter(ips)


# def get_frequent_visit_from_ip(ips):
#     return get_count_visits_from_ip(ips).most_common(1)[0]
    
    
    
    
# Cat = collections.namedtuple("Cat", ["nickname", "age", "owner"])
# cat = Cat(nickname='Mick', age=5, owner='Sara')
# print(type(cat))
# cats = [Cat(nickname='Mick', age=5, owner='Sara'), Cat(nickname='Barsik', age=7, owner='Olga'), Cat(nickname='Simon', age=3, owner='Yura')]


# dict1 = [{'nickname': cat.nickname, 'age': cat.age, 'owner': cat.owner} for cat in cats]
# print(dict1)
# def convert_list(cats: Cat):
#     for cat in cats:
#         if isinstance(cat, dict):
#             return [Cat(*cat.values()) for cat in cats]
#         elif isinstance(cat, tuple):
#             return [{'nickname': cat.nickname, 'age': cat.age, 'owner': cat.owner} for cat in cats]
            

# print(convert_list([
#     {"nickname": "Mick", "age": 5, "owner": "Sara"},
#     {"nickname": "Barsik", "age": 7, "owner": "Olga"},
#     {"nickname": "Simon", "age": 3, "owner": "Yura"},
# ]))
# У нас є іменований кортеж для зберігання котів у змінній Cat. На першому місці у нас кличка котика nickname, потім його вік age та ім'я власника кота owner.

# Напишіть функцію convert_list(cats), яка працюватиме у двох режимах.

# Якщо функція convert_list приймає у параметрі cats список іменованих кортежів

# [Cat("Mick", 5, "Sara"), Cat("Barsik", 7, "Olga"), Cat("Simon", 3, "Yura")]
# То функція поверне наступний список словників:

# [
#     {"nickname": "Mick", "age": 5, "owner": "Sara"},
#     {"nickname": "Barsik", "age": 7, "owner": "Olga"},
#     {"nickname": "Simon", "age": 3, "owner": "Yura"},
# ]
# І в той же час, якщо функція convert_list приймає в параметрі cats список словників, то результатом буде зворотна операція та функція поверне список іменованих кортежів.

# Для визначення типу параметра cats використовуйте функцію isinstance.











# def decimal_average(number_list, signs_count):
#     getcontext().prec = signs_count
#     return sum(map(Decimal, number_list)) / len(number_list)


# participants = {
#     "603d2cec9993c627f0982404": "test@test.com",
#     "603f79022922882d30dd7bb6": "test11@test.com",
#     "60577ce4b536f8259cc225d2": "test2@test.com",
#     "605884760742316c07eae603": "vitanlhouse@gmail.com",
#     "605b89080c318d66862db390": "elhe2013@gmail.com",
# }


# def get_random_winners(quantity: int, participants: dict):
#     if quantity > len(participants):
#         return []
#     id_list = list(participants.keys())
#     random.shuffle(id_list)
#     return random.sample(id_list, quantity)
    
# def get_numbers_ticket(min, max, quantity):
#     if not(min < quantity < max) or min < 1 or max > 1000:
#         return[]  
#     no_dubl = set()
#     while len(no_dubl) != quantity:
#         no_dubl.add(randrange(min, max + 1))
#     return sorted(list(no_dubl))  


# print(datetime.now())
# print(get_random_winners(10, participants))  
# print(datetime.now())












# def get_str_date(date: str):
#     split_date = date.split(' ')[0].split('-')
#     return datetime(*map(int, split_date)).strftime('%A %d %B %Y')
    
    
  

# def get_days_in_month(month, year, day=1):
#     user_date = date(year, month, day)
#     return (user_date.replace(month=month + 1) - user_date).days if month != 12 else (user_date.replace(year=year+1, month=1) - user_date).days
    # return abs((datetime(year, month, 1) - datetime(year, month - 1, 1)).days) if month == 12 else abs((datetime(year, month, 1) - datetime(year, month + 1, 1)).days)
    
    
# def get_days_from_today(date: str):
#     return (datetime.now() - datetime(*map(int, date.split('-')))).days


















# def encode(data):
#     result = []
#     for i in range(1, len(data)):
#         if data[i] != data[i-1]:
#             result.extend([data[i-1], i])
#             result.extend(decode(data[i:]))
#             break
#         if i + 1 == len(data):
#             result.extend([data[i], i+1])
#     return result










# def decode(data):
#     result = []
#     for i in range(1, len(data)):
#         if type(data[i]) == int:
#             result.extend([data[i-1]] * data[i])
#             result.extend(decode(data[i+1:]))
#             break
#     return result


# print(decode(["X", 3, "Z", 2, "X", 2, "Y", 3, "Z", 2]))


# ["X", "X", "X", "Z", "Z", "X", "X", "Y", "Y", "Y", "Z", "Z"]
# def flatten(data: list):
#     # print(len(data))
#     # global result
#     result = []
#     for el in data:
#         if type(el) == list:
#             result.extend(flatten(el))
#         else:
#             result.append(el)  
#     return result


# print(flatten([1, [2, 3], [4, [5, [6, 7]]], [[[8], 9], [10]]]))


# def to_indexed(source_file, output_file):
#     lines_list = []
#     with open(source_file, 'r') as fl_r:
#         lines_list = fl_r.readlines()
        
#     for number, line in enumerate(lines_list):
#         lines_list[number] = f'numebr: {line}'
    
#     with open(source_file, 'w') as fl_w:
#         fl_w.writelines(lines_list)


# def get_employees_by_profession(path, profession):
#     workers_list = ''
#     with open(path, 'r') as fl_r:
#         workers_list = fl_r.readlines()
        
#     worker_with_current_profession = [worker.split()[0] for worker in workers_list if profession in worker]
    
#     return ' '.join(worker_with_current_profession)
 
# def file_operations(path, additional_info, start_pos, count_chars):
#     with open(path, 'a') as fl_w:
#         fl_w.write(additional_info)
    
#     with open(path, 'r') as fl_r:
#         fl_r.seek(start_pos)
#         return fl_r.read(count_chars)

# char_list= [' ', '.,?!:', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
# translate_dict = {}
# for i, elem in enumerate(char_list, 0):
#     for number, char in enumerate(elem, 1):
#         translate_dict[ord(char)] = str(i) * number
#         translate_dict[ord(char.upper())] = str(i) * number
        

# def sequence_buttons(string: str):
#     return string.translate(translate_dict)

# print(sequence_buttons('Hello, World!'))
    

# def make_request(keys, values):
#     if len(keys) == len(values):
#         return dict(zip(keys, values))
#     return {}

# def all_sub_lists(data):
#     a = [[]]
#     for i in range(1, len(data) + 1):
#         for j in range(len(data)):
#             if i == len(data[j:j + i]):
#                 a.append(data[j:j + i])
#     return a



# print(all_sub_lists([]))
# def token_parser(data: str):
#     return list(filter(None, re.split(r'(\(|\)|\+|-|\*|/|=)', re.sub(' ', '', data))))
    # (\(|\)|\+|-|\*|/|=)
    
# print(token_parser("2+ 34-5 * 3"))
# def data_preparation(list_data):
#     new_list_data = []
#     for lst in list_data:
#         new_list_data.extend(filter(lambda x: x not in (min(lst), max(lst)), lst) if len(lst) >= 3 else lst)
    
#     return sorted(new_list_data, reverse=True)    
    
    
    
# print(data_preparation([[1, 2, 3, 0], [3], [5, 6, 1, 7, 2]]))    
    
    
    
    
    
    
    
    
    
    
    
# def solve_riddle(riddle: str, word_length, start_letter, reverse=False):
#     start_letter_position = 0
#     result = ''
#     if start_letter not in riddle:
#         return ''
#     if reverse:
#         start_letter_position = riddle.rindex(start_letter)
#         result = riddle[start_letter_position - word_length+1:start_letter_position+1][::-1]
        
#     else:
#         start_letter_position = riddle.index(start_letter)
#         result = riddle[start_letter_position:start_letter_position + word_length]
    
#     return result




# solve_riddle('aaatttrrr', 5, 'p')


# def get_match(m: re.Match):
#     return f'{m.group()}'.upper()


# def capital_text(data: str):
    
#     return re.sub(r'([!?.] \w|\A\w)', get_match, data)
    

# print(capital_text('alert. boss! oh'))

# 'alert. boss! oh'
# 'hello world! awesome? yes'

    
# files = glob.glob(MAIN_PATH + '/**', recursive=True)
# p = pathlib.Path(MAIN_PATH)
# files2 = p.rglob('**')
# print(*files, sep='\n')
# print(*files2, sep='\n')
# files2 = list(files2)
# print(*files2, sep='\n')
# os.rename('text.txt', 'text1.txt')

# import glob

# files = glob.glob(MAIN_PATH + '/**', recursive=True)
# print(*files, sep='\n')


# for root, dirs, files in os.walk(MAIN_PATH):
#    for dir_ in dirs:
#       print(os.path.join(root, dir_))

# list_subfolders_with_paths = [x for x in p.iterdir() if x.is_dir()]
# list_subfolders_with_paths_scan = [f.path for f in os.scandir(MAIN_PATH) if f.is_dir()]
# print(*list_subfolders_with_paths, sep='\n')
# print()
# print(*list_subfolders_with_paths_scan, sep='\n')

# def get_path(path):
#     p = pathlib.Path(path)
#     list_subfolders_with_paths = [x for x in p.iterdir() if x.is_dir()]
#     if not list_subfolders_with_paths:
#         return path
#     else:
#         return [get_path(x) for x in list_subfolders_with_paths]
    
# print(*get_path(MAIN_PATH), sep='\n')

    # print(len(list_subfolders_with_paths))
# a = list(extensions.items())
# print(a[0])

# p = pathlib.Path('D:\Go It projects\Git')
# print([x for x in p.iterdir()])

# print(list(p.glob('**/')))

# print(p.parent)
# print(p.name)
# print(p.suffix)










# def create_backup(path, file_name, employee_residence):
#     with open(f'{path}/{file_name}', 'wb') as fl_wb:
#         for key, value in employee_residence.items():
#             fl_wb.write(f'{key} {value}\n'.encode())
            
#     archive_path = shutil.make_archive('backup_folder', 'zip', path)           
#     return archive_path
    
# print(create_backup('archive', 'test_archive.bin', {'Michael': 'Canada', 'John':'USA', 'Liza': 'Australia'}))    


# def unpack(archive_path, path_to_unpack):
#     shutil.unpack_archive(archive_path, path_to_unpack)

# unpack(r'D:\Go It projects\Git\goit-projects\backup_folder.zip', r'D:\Go It projects\Git\goit-projects\archive')


# Реалізуйте функцію create_archive(path, file_name, employee_residence)

# Де:

# path — шлях до файлу
# file_name — ім'я файлу
# employee_residence — словник, у якому ключ — ім'я користувача, а значення — країна проживання. Вигляд: {'Michael': 'Canada', 'John':'USA', 'Liza': 'Australia'}
# Функція повинна працювати так:

# Створювати бінарний файл file_name за шляхом path
# Зберігати дані словника employee_residence у файл, де кожен новий рядок — це ключ значення через пробіл як "Michael Canada"
# Архівувати теку по шляху path за допомогою shutil
# Ім'я архіву має бути 'backup_folder.zip'
# Функція має повернути рядок шляху до архіву 'backup_folder.zip'
# Вимоги:

# запишіть вміст словника employee_residence у бінарний файл з ім'ям file_name у теку path за допомогою оператора with.
# використовуйте символ /, щоб розділити шлях для path та file_name
# вигляд рядка файлу — Michael Canada, в кінці кожного рядка додається перенесення рядка '\n'.
# при збереженні кожен рядок файлу кодується методом encode
# при записі рядків використовуємо лише метод write
# архів має бути у форматі zip з ім'ям 'backup_folder', створений за допомогою make_archive.








# def encode_data_to_base64(data: list):
#     return [base64.b64encode(el.encode()).decode() for el in data]



# print(encode_data_to_base64(['andry:uyro18890D', 'steve:oppjM13LL9e']))

# def save_credentials_users(path, users_info: dict):
#     with open(path, 'wb') as fl_wb:
#         for key, value in users_info.items():
#             string = f'{key}:{value}\n'
#             fl_wb.write(string.encode())


# def get_credentials_users(path):
#     with open(path, 'rb') as fl_rb:
#         return [el.decode().replace('\n', '') for el in fl_rb.readlines()]


# print('Hello'.encode('utf-'))

# save_credentials_users('test.bin', {'andry':'uyro18890D', 'steve':'oppjM13LL9e'})
# print(get_credentials_users('test.bin'))

# def is_equal_string(utf8_string: bytes, utf16_string: bytes):
#     return utf8_string.decode('utf-8').casefold() == utf16_string.decode('utf-16').casefold()

# students = [
#     {
#         "name": "Kovalchuk Oleksiy",
#         "specialty": 301,
#         "math": 175,
#         "lang": 180,
#         "eng": 155,
#     },
#     {
#         "name": "Ivanchuk Boryslav",
#         "specialty": 101,
#         "math": 135,
#         "lang": 150,
#         "eng": 165,
#     },
#     {
#         "name": "Karpenko Dmitro",
#         "specialty": 201,
#         "math": 155,
#         "lang": 175,
#         "eng": 185,
#     },
# ]
# def save_applicant_data(source: list, output):
#     with open(output, 'w') as fl:
#         for el in source:
#             fl.write(','.join(map(str, el.values())) + '\n')

# save_applicant_data(students, 'test.txt')




# def sanitize_file(source, output):
#     with open(source, 'r') as fl_r:
#         text = re.sub(r'[\d]', '', fl_r.read())
#         with open(output, 'w') as fl_w:
#             fl_w.write(text)


# sanitize_file('test.txt', 'text.txt')            

# def get_recipe(path, search_id):
#     with open(path, 'r') as fl:
#         while True:
#             line = fl.readline()
#             if not line:
#                 break
#             if search_id in line:
#                 _id, name, *ingredients = line.replace('\n', '').split(',')
#                 return {'id': _id, 'name': name, 'ingredients': ingredients}
                
                

# print(get_recipe('test.txt', '60b90c3b13067a15887e1ae4'))

# a, b, *c = '60b90c3b13067a15887e1ae4,Watermelon Cucumber Salad,1 large seedless watermelon,12 leaves fresh mint,1 cup crumbled feta cheese'.split(',')

# print(a, b ,c)


# def get_cats_info(path):
#     with open(path, 'r') as fl:
#         return [{key: value for key, value in zip(['id','name','age'], lines.replace('\n', '').split(','))} for lines in fl.readlines()]


# # print(*zip(['id','name','age'], '60b90c1c13067a15887e1ae1,Tayson,3'.split(',')))
# print(get_cats_info('test.txt'))

# a, b, c = '60b90c1c13067a15887e1ae1,Tayson,3'.split(',')
# print(a, b, c)
# def write_employees_to_file(employee_list, path):
#     fl = open(path, 'w')
#     new_empl_list = [element + '\n' for lst in employee_list for element in lst]
#     for employee in new_empl_list:
#         fl.write(employee)
#     fl.close()    


# def read_employees_from_file(path):
#     fl = open(path, 'r')
#     result = []
#     while True:
#         line = fl.readline().replace('\n', '')
#         if not line:
#             fl.close()
#             break
#         result.append(line)
#     return result



# def add_employee_to_file(record, path):
#     fl = open(path, 'a')
#     fl.write(record + '\n')
#     fl.close()
    
# write_employees_to_file([['Robert Stivenson,28', 'Alex Denver,30'], ['Drake Mikelsson,19']], 'text.txt')
# print(read_employees_from_file('text.txt'))
# add_employee_to_file('Drake Mikelsson,19', 'text.txt')
# a = [['Robert Stivenson,28', 'Alex Denver,30'], ['Drake Mikelsson,19']]

# b = []
# b.extend(a[0])
# b.extend(a[1])
# print(b)
         
# c = [e for el in a for e in el]

# print(c)
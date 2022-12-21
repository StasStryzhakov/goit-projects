
from collections import UserString
import re
from random import randrange
import csv
import pickle
import json

import re


char_list= [' ', '.,?!:', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
translate_dict = {}
for i, elem in enumerate(char_list, 0):
    for number, char in enumerate(elem, 1):
        translate_dict[ord(char)] = str(i) * number
        translate_dict[ord(char.upper())] = str(i) * number
        

def sequence_buttons(string: str):
    return string.translate(translate_dict)

print(sequence_buttons("Hello, World!"))





# def get_match(m: re.Match):
#     return f'{m.group()}'.upper()


# def capital_text(s: str):
    
#     return re.sub(r'([!?.] \w|\A\w)', get_match, s)

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


# class ListedValuesDict:
#     def __init__(self):
#         self.data = {}

#     def __setitem__(self, key, value):
#         if key in self.data:
#             self.data[key].append(value)
#         else:
#             self.data[key] = [value]

#     def __getitem__(self, key):
#         result = str(self.data[key][0])
#         for value in self.data[key][1:]:
#             result += ", " + str(value)
#         return result


# l_dict = ListedValuesDict()
# l_dict[1] = 'a'
# l_dict[1] = 'b'
# print(l_dict[1]) 
# a, b
# class Person:
#     def __init__(self, name: str, email: str, phone: str, favorite: bool):
#         self.name = name
#         self.email = email
#         self.phone = phone
#         self.favorite = favorite


# class Contacts:
    
    
#     def __init__(self, filename: str, contacts: list[Person] = None, count_save = 0):
#         if contacts is None:
#             contacts = []
            
#         self.count_save = count_save
#         self.filename = filename
#         self.contacts = contacts
        
#     def __getstate__(self):
#         atr = self.__dict__.copy()
#         atr['count_save'] += 1
#         return atr    

#     def save_to_file(self):
#         with open(self.filename, "wb") as file:
#             pickle.dump(self, file)

#     def read_from_file(self):
#         with open(self.filename, "rb") as file:
#             content = pickle.load(file)
#         return content

    
        
        
# contacts = [
#     Person(
#         "Allen Raymond",
#         "nulla.ante@vestibul.co.uk",
#         "(992) 914-3792",
#         False,
#     ),
#     Person(
#         "Chaim Lewis",
#         "dui.in@egetlacus.ca",
#         "(294) 840-6685",
#         False,
#     ),
# ]        
# persons = Contacts("user_class.dat", contacts)
# persons.save_to_file()

# first = persons.read_from_file()
# first.save_to_file()
# second = first.read_from_file()
# second.save_to_file()
# third = second.read_from_file()

# print(persons.count_save)  # 0
# print(first.count_save)  # 1
# print(second.count_save)  # 2
# print(third.count_save)  # 3

# class Person:
#     def __init__(self, name: str, email: str, phone: str, favorite: bool):
#         self.name = name
#         self.email = email
#         self.phone = phone
#         self.favorite = favorite
        
        
        


# class Contacts:
#     def __init__(self, filename: str, contacts: list[Person] = None):
#         if contacts is None:
#             contacts = []
#         self.filename= filename
#         self.contacts = contacts
        
        
        

#     def save_to_file(self):
#         with open(self.filename, 'wb') as fw:
#             pickle.dump(self, fw) 
                   
            

#     def read_from_file(self):
#         with open(self.filename, 'rb') as fr:
#             return pickle.load(fr)




# contacts = [
#     Person(
#         "Allen Raymond",
#         "nulla.ante@vestibul.co.uk",
#         "(992) 914-3792",
#         False,
#     ),
#     Person(
#         "Chaim Lewis",
#         "dui.in@egetlacus.ca",
#         "(294) 840-6685",
#         False,
#     ),
# ]

# persons = Contacts("user_class.dat", contacts)

# persons.save_to_file()
# person_from_file = persons.read_from_file()

# print(persons == person_from_file)  # False
# print(persons.contacts[0] == person_from_file.contacts[0])  # False
# print(persons.contacts[0].name == person_from_file.contacts[0].name)  # True
# print(persons.contacts[0].email == person_from_file.contacts[0].email)  # True
# print(persons.contacts[0].phone == person_from_file.contacts[0].phone) # True












# def write_contacts_to_file(filename, contacts):
#     with open(filename, 'w', newline='') as fw:
#         field_names = ["name", "email", "phone", "favorite"]
#         writer = csv.DictWriter(fw, fieldnames=field_names)
#         writer.writeheader()
#         for contact in contacts:
#             writer.writerow(contact)
    
        
        
        
            


# def read_contacts_from_file(filename):
#     with open(filename, newline='') as fr:
#         reader = csv.DictReader(fr)
#         result = []    
#         for row in reader:
#             row['favorite'] = True if row['favorite'] == 'True' else False
#             result.append(row)
#         return result
        
        
    
    
    
# contacts = [{
#     "name": "Allen Raymond",
#     "email": "nulla.ante@vestibul.co.uk",
#     "phone": "(992) 914-3792",
#     "favorite": False,
# },{
#     "name": "Allen Raymond",
#     "email": "nulla.ante@vestibul.co.uk",
#     "phone": "(992) 914-3792",
#     "favorite": False,
# }]    
    
# write_contacts_to_file("contacts_list.csv", contacts)
# print(read_contacts_from_file("contacts_list.csv"))
# read_contacts_from_file("contacts_list.csv")
    
    
    
    

# def write_contacts_to_file(filename, contacts):
#     with open(filename, 'wb') as fw:
#         json.dump(contacts, fw)
        


# def read_contacts_from_file(filename):
#     with open(filename, 'rb') as fr:
#         return json.load(fr)


# with open('names.csv', 'w', newline='') as fh:
#     field_names = ['first_name', 'last_name']
#     writer = csv.DictWriter(fh, fieldnames=field_names)
#     writer.writeheader()
#     writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
#     writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
#     writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})


# with open('names.csv', newline='') as fh:
#     reader = csv.DictReader(fh)
#     for row in reader:
#         print(row['first_name'], row['last_name'])
        
        
        

        

# with open('eggs.csv', 'w', newline='') as fh:
#     spam_writer = csv.writer(fh)
#     spam_writer.writerow(['Spam'] * 5 + ['Baked Beans'])
#     spam_writer.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])


# with open('eggs.csv', newline='') as fh:
#     spam_reader = csv.reader(fh)
#     for row in spam_reader:
#         print(', '.join(row))
        
# class Point:
#     def __init__(self, x, y):
#         self.__x = None
#         self.__y = None
#         self.x = x
#         self.y = y

#     @property
#     def x(self):
#         return self.__x

#     @x.setter
#     def x(self, x):
#         if (type(x) == int) or (type(x) == float):
#             self.__x = x

#     @property
#     def y(self):
#         return self.__y

#     @y.setter
#     def y(self, y):
#         if (type(y) == int) or (type(y) == float):
#             self.__y = y

#     def __str__(self):
#         return f"Point({self.x},{self.y})"


# class Vector:
#     def __init__(self, coordinates: Point):
#         self.coordinates = coordinates

#     def __setitem__(self, index, value):
#         if index == 0:
#             self.coordinates.x = value
#         if index == 1:
#             self.coordinates.y = value

#     def __getitem__(self, index):
#         if index == 0:
#             return self.coordinates.x
#         if index == 1:
#             return self.coordinates.y

#     def __call__(self, value=None):
#         if value:
#             self.coordinates.x = self.coordinates.x * value
#             self.coordinates.y = self.coordinates.y * value
#         return self.coordinates.x, self.coordinates.y

#     def __add__(self, vector):
#         x = self.coordinates.x + vector.coordinates.x
#         y = self.coordinates.y + vector.coordinates.y
#         return Vector(Point(x, y))

#     def __sub__(self, vector):
#         x = self.coordinates.x - vector.coordinates.x
#         y = self.coordinates.y - vector.coordinates.y
#         return Vector(Point(x, y))

#     def __mul__(self, vector):
#         return (
#                 self.coordinates.x * vector.coordinates.x
#                 + self.coordinates.y * vector.coordinates.y
#         )

#     def len(self):
#         return (self.coordinates.x ** 2 + self.coordinates.y ** 2) ** 0.5

#     def __str__(self):
#         return f"Vector({self.coordinates.x},{self.coordinates.y})"
    

#     def __eq__(self, vector):
#         return self.coordinates.x == vector.coordinates.x and self.coordinates.y == vector.coordinates.y

#     def __ne__(self, vector):
#         return self.coordinates.x != vector.coordinates.x or self.coordinates.y != vector.coordinates.y

#     def __lt__(self, vector):
#         return self.coordinates.x < vector.coordinates.x and self.coordinates.y < vector.coordinates.y

#     def __gt__(self, vector):
#         return self.coordinates.x > vector.coordinates.x and self.coordinates.y > vector.coordinates.y

#     def __le__(self, vector):
#         return self.coordinates.x <= vector.coordinates.x and self.coordinates.y <= vector.coordinates.y

#     def __ge__(self, vector):
#         return self.coordinates.x >= vector.coordinates.x and self.coordinates.y >= vector.coordinates.y


# class Iterable:
#     def __init__(self, max_vectors, max_points):
#         self.current_index = 0
#         self.max_vectors = max_vectors
#         self.max_points = max_points
#         self.vectors = [Vector(Point(randrange(0, self.max_points), randrange(0, self.max_points))) for _ in range(max_vectors)]
        
        
            

#     def __next__(self):
        
#         try:
#             result = self.vectors[self.current_index]
#             self.current_index += 1
#             return result
#         except IndexError:
#             raise StopIteration
            
            
            
        
            


# class RandomVectors:
#     def __init__(self, max_vectors=10, max_points=50):
#         self.max_vecors = max_vectors
#         self.max_points = max_points
        

#     def __iter__(self):
#         return Iterable(self.max_vecors, self.max_points)
    
# vectors = RandomVectors(5, 10)

# for vector in vectors:
#     print(vector)    

# print(Vector(Point(0, 0)) == Vector(Point(0, 0)))  # True
# print(Vector(Point(0, 0)) != Vector(Point(0, 0)))  # True
# print(Vector(Point(0, 0)) < Vector(Point(1, 1)))  # True
# print(Vector(Point(1, 1)) > Vector(Point(0, 0)))  # True
# print(Vector(Point(1, 1)) <= Vector(Point(1, 2)))  # True
# print(Vector(Point(2, 1)) >= Vector(Point(2, 0)))  # True


# class Point:
#     def __init__(self, x, y):
#         self.__x = None
#         self.__y = None
#         self.x = x
#         self.y = y

#     @property
#     def x(self):
#         return self.__x

#     @x.setter
#     def x(self, x):
#         if (type(x) == int) or (type(x) == float):
#             self.__x = x

#     @property
#     def y(self):
#         return self.__y

#     @y.setter
#     def y(self, y):
#         if (type(y) == int) or (type(y) == float):
#             self.__y = y

#     def __str__(self):
#         return f"Point({self.x},{self.y})"


# class Vector:
#     def __init__(self, coordinates: Point):
#         self.coordinates = coordinates

#     def __setitem__(self, index, value):
#         if index == 0:
#             self.coordinates.x = value
#         if index == 1:
#             self.coordinates.y = value

#     def __getitem__(self, index):
#         if index == 0:
#             return self.coordinates.x
#         if index == 1:
#             return self.coordinates.y

#     def __call__(self, value=None):
#         if value:
#             self.coordinates.x = self.coordinates.x * value
#             self.coordinates.y = self.coordinates.y * value
#         return self.coordinates.x, self.coordinates.y

#     def __add__(self, vector):
#         x = self.coordinates.x + vector.coordinates.x
#         y = self.coordinates.y + vector.coordinates.y
#         return Vector(Point(x, y))

#     def __sub__(self, vector):
#         x = self.coordinates.x - vector.coordinates.x
#         y = self.coordinates.y - vector.coordinates.y
#         return Vector(Point(x, y))
        
        

#     def __str__(self):
#         return f"Vector({self.coordinates.x},{self.coordinates.y})"



# vector1 = Vector(Point(1, 1))
# vector2 = Vector(Point(3, 3))

# vector3 = vector2 - vector1

# print(vector3)

# class Point:
#     def __init__(self, x, y):
#         self.__x = None
#         self.__y = None
#         self.x = x
#         self.y = y

#     @property
#     def x(self):
#         return self.__x

#     @x.setter
#     def x(self, x):
#         if (type(x) == int) or (type(x) == float):
#             self.__x = x

#     @property
#     def y(self):
#         return self.__y

#     @y.setter
#     def y(self, y):
#         if (type(y) == int) or (type(y) == float):
#             self.__y = y

#     def __str__(self):
#         return f"Point({self.x},{self.y})"


# class Vector:
#     def __init__(self, coordinates: Point):
#         self.coordinates = coordinates

#     def __setitem__(self, index, value):
#         if index == 0:
#             self.coordinates.x = value
#         if index == 1:
#             self.coordinates.y = value

#     def __getitem__(self, index):
#         if index == 0:
#             return self.coordinates.x
#         if index == 1:
#             return self.coordinates.y

#     def __call__(self, value=None):
#         if (type(value) == int) or (type(value) == float):
#             return (self.coordinates.x * value, self.coordinates.y * value)
#         else:
#             return (self.coordinates.x, self.coordinates.y)
            
            
        

#     def __str__(self):
#         return f"Vector({self.coordinates.x},{self.coordinates.y})"
    
    
# vector = Vector(Point(1, 10))

# print(vector())
# print(vector(5))
# vector[1] = 999
# print(vector[1])

# class Point:
#     def __init__(self, x, y):
#         self.__x = None
#         self.__y = None
#         self.x = x
#         self.y = y

#     @property
#     def x(self):
#         return self.__x

#     @x.setter
#     def x(self, x):
#         if (type(x) == int) or (type(x) == float):
#             self.__x = x

#     @property
#     def y(self):
#         return self.__y

#     @y.setter
#     def y(self, y):
#         if (type(y) == int) or (type(y) == float):
#             self.__y = y

#     def __str__(self):
#         return f'Point({self.x},{self.y})'
        


# class Vector:
#     def __init__(self, coordinates: Point):
#         self.coordinates = coordinates

#     def __setitem__(self, index, value):
#         if index == 0:
#             self.coordinates.x = value
#         if index == 1:
#             self.coordinates.y = value

#     def __getitem__(self, index):
#         if index == 0:
#             return self.coordinates.x
#         if index == 1:
#             return self.coordinates.y

#     def __str__(self):
#         return f'Vector({self.coordinates.x},{self.coordinates.y})'
        
        
# class Point:
#     def __init__(self, x, y):
#         self.__x = None
#         self.__y = None
#         self.x = x
#         self.y = y

#     @property
#     def x(self):
#         return self.__x

#     @x.setter
#     def x(self, x):
#         if (type(x) == int) or (type(x) == float):
#             self.__x = x

#     @property
#     def y(self):
#         return self.__y

#     @y.setter
#     def y(self, y):
#         if (type(y) == int) or (type(y) == float):
#             self.__y = y


# class Vector:
#     def __init__(self, coordinates: Point):
#         self.coordinates = coordinates
#         self.position = [self.coordinates.x, self.coordinates.y]

#     def __setitem__(self, index, value):
#         self.position[index] = value
            
        
            

#     def __getitem__(self, index):
#         return self.position[index]
        
        
        
# class Point:
#     def __init__(self, x, y):
#         self.__x = None
#         self.__y = None
#         self.x = x
#         self.y = y
        
#     @property
#     def x(self):
#         return self.__x
    
#     @x.setter
#     def x(self, new_x):
#         if type(new_x) in (int, float):
#             self.__x = new_x
        
        
#     @property
#     def y(self):
#         return self.__y
    
#     @y.setter
#     def y(self, new_y):
#         if type(new_y) in (int, float):
#             self.__y = new_y
        
# point = Point('5', 10)

# print(point.x)  # 5
# print(point.y)  # 10

# point.x = 10
# point.y = 15

# print(point.x)
# print(point.y)



# class Contacts:
#     current_id = 1

#     def __init__(self):
#         self.contacts = []

#     def list_contacts(self):
#         return self.contacts

#     def add_contacts(self, name, phone, email, favorite):
#         self.contacts.append(
#             {
#                 "id": Contacts.current_id,
#                 "name": name,
#                 "phone": phone,
#                 "email": email,
#                 "favorite": favorite,
#             }
#         )
#         Contacts.current_id += 1

#     def get_contact_by_id(self, id):
#         if 0 < (id - 1) <= len(self.contacts):
#             return self.contacts
        
# a = Contacts()
# a.add_contacts('Stas', 123123123,'dfsadf@.com', True)
# a.add_contacts('Vovva', 123123123,'dfsadf@.com', True)

# print(a.list_contacts())
# print(a.get_contact_by_id(0))

# class Contacts:
#     current_id = 1

#     def __init__(self):
#         self.contacts = []

#     def list_contacts(self):
#         return self.contacts
    
#     def add_contacts(self, name, phone, email, favorite):
#         self.contacts.append({'id': Contacts.current_id, 'name': name, 'phone': phone, 'email': email, 'favorite': favorite})
#         Contacts.current_id += 1
        
        
# class Animal:
#     def __init__(self, nickname, weight):
#         self.nickname = nickname
#         self.weight = weight

#     def say(self):
#         pass

#     def change_weight(self, weight):
#         self.weight = weight


# class Cat(Animal):
#     def say(self):
#         return "Meow"


# class CatDog:
#     def __init__(self, nickname, weight):
#         self.nickname = nickname
#         self.weight = weight
        
#     def say(self):
#         return 'WoofMeow'
    
#     def change_weight(self, weight):
#         self.weight = weight
    


    
    

# class IDException(Exception):
#     pass


# def add_id(id_list, employee_id: str):
#     if not employee_id.startswith('01'):
#         raise IDException
#     else:
#         return id_list.append(employee_id)
    
    
    
# class NumberString(UserString):
#     def number_count(self):
#         return len(re.findall('\d', self.data))



# from collections import UserList


# class AmountPaymentList(UserList):
#     def amount_payment(self):
#         return sum(filter(lambda x: x > 0, self.data))
    
    
    
    
# from collections import UserDict


# class LookUpKeyDict(UserDict):
#     def lookup_key(self, value):
#         return [key for key, val in self.data.items() if val == value]
        


# class Animal:
#     def __init__(self, nickname, weight):
#         self.nickname = nickname
#         self.weight = weight

#     def say(self):
#         pass


# class Cat(Animal):
#     def say(self):
#         return "Meow"


# class Dog(Animal):
#     def say(self):
#         return "Woof"
    
# class CatDog(Cat, Dog):
#     def info(self):
#         return f"{self.nickname}-{self.weight}"

# class DogCat(Dog, Cat):
#     def info(self):
#         return f"{self.nickname}-{self.weight}"





# class Animal:
#     def __init__(self, nickname, weight):
#         self.nickname = nickname
#         self.weight = weight

#     def say(self):
#         pass

#     def change_weight(self, weight):
#         self.weight = weight


        
# class Owner:
#     def __init__(self, name, age, adress):
#         self.name = name
#         self.age = age
#         self.adrees= adress
        
        
#     def info(self):     
#         return {'name': self.name, 'age': self.age, 'adress': self.adrees}

# class Dog(Animal):
#     def __init__(self, nickname, weight, owner: Owner):
#         self.owner = owner
#         super().__init__(nickname, weight)
        
#     def who_is_owner(self):
#         return self.owner.info()    




# owner = Owner("Sherlock", 24, "London, 221B Baker Street")
# dog = Dog("Simon", 10, owner)
# print(owner.info())
# print(dog.who_is_owner())






















# class Animal:
#     def __init__(self, nickname, weight):
#         self.nickname = nickname
#         self.weight = weight

#     def say(self):
#         pass

#     def change_weight(self, weight):
#         self.weight = weight


# class Cat(Animal):
    
#     def say(self):
#         return 'Meow'
        
    
# class Dog(Animal):
#     def __init__(self, nickname, weight, breed):
#         super().__init__(nickname, weight)
#         self.breed = breed
        
#     def say(self):
#         return 'Woof'
        
        
        
        
# cat = Cat('Simon', 10)














# def get_emails(list_contacts):
#     # return [element.get('email') for element in list_contacts]
#     return list(map(lambda x: x.get('email'), list_contacts))


# print(get_emails([{
#     "name": "Allen Raymond",
#     "email": "nulla.ante@vestibul.co.uk",
#     "phone": "(992) 914-3792",
#     "favorite": False,
# },{
#     "name": "Allen Raymond",
#     "email": "nulla.ante@vestibul.co.uk",
#     "phone": "(992) 914-3792",
#     "favorite": False,
# }]))




# def normal_name(list_name):
#     return map(str.title, list_name)

# def generator_numbers(string):
#     for number in re.findall(r'\d+', string):
#         yield number
    
    

# def sum_profit(string):
#     return sum(map(int, string))
        
        
        
            
            
                
                
# print(sum_profit(generator_numbers("The resulting profit was: from the southern possessions $ 100, from the northern colonies $500, and the king gave $1000.")))
        
            
    
    
# def format_phone_number(func):
#     def inner(phone):
#         sanitize_phone = func(phone)
#         return f'+{sanitize_phone}' if len(sanitize_phone) == 12 else f'+38{sanitize_phone}'
#     return inner
        

# @format_phone_number
# def sanitize_phone_number(phone):
#     return re.sub('[()+ -]', '', phone)



# print(sanitize_phone_number("(050)8889900"))



# def discount_05(price):
#     return price * (1 - 0.05)

# def discount_10(price):    
#     return price * (1 - 0.10)

# def discount_15(price):    
#     return price * (1 - 0.15)

# def discount_0(price):
#     return price

# def discount_25(price):    
#     return price * (1 - 0.25)

# DISCOUNT_OPERATION = {0: discount_0,
#                       0.05: discount_05,
#                       0.10: discount_10,
#                       0.15: discount_15,
#                       0.25: discount_25}


# def discount_price(discount):
#     return DISCOUNT_OPERATION[discount]




# cost_15 = discount_price(0.15)
# cost_10 = discount_price(0.10)
# cost_05 = discount_price(0.05)
# cost_0 = discount_price(0)

# price = 100
# print(cost_15(price))
# print(cost_10(price))
# print(cost_05(price))
# print(cost_0(price))










# def caching_fibonacci():
#     cache = {}    
#     def fibonacci(n):
#         if n <= 1:
#             return cache.setdefault(n, 1)
#         return cache.get(n, fibonacci(cache.get(n-1)) + fibonacci(cache.get(n-2)))

#     return fibonacci



# fibonaci = caching_fibonacci()

# print(fibonaci(5))



# def caching_fibonacci():
#     cache = {}
#     def fibonacci(n):
#         if n in (1, 2):
#             return cache.setdefault(n, n-1)
        
#         return cache.setdefault(n, fibonacci(n - 1) + fibonacci(n - 2))
#     return fibonacci

# f = caching_fibonacci()
# print(f(7))







# DEFAULT_DISCOUNT = 0.05


# def get_discount_price_customer(price, customer):
#     global DEFAULT_DISCOUNT
#     return price * (1 - customer.get('discount', DEFAULT_DISCOUNT))
    
    
    
    
# def get_grade(key):
#     grade = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}
#     return grade.get(key, None)


# def get_description(key):
#     description = {
#         "A": "Perfectly",
#         "B": "Very good",
#         "C": "Good",
#         "D": "Satisfactorily",
#         "E": "Enough",
#         "FX": "Unsatisfactorily",
#         "F": "Unsatisfactorily",
#     }
#     return description.get(key, None)


# def get_student_grade(option):
#     value = {'grade': get_grade,
#              'description': get_description}
#     return value.get(option, None)




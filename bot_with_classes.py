from collections import UserDict

class Field:
    pass

class Name(Field):
    def __init__(self, name: str):
        self.name = name

class Phone(Field):
    def __init__(self, phone: str):
        self.phone = phone

class Record:
    
    def __init__(self, name: Name, phone=None):
        self.name = name
        self.phones = []
        if phone:
            self.phones.append(phone)
        
    
    def add_phone(self, phone: Phone):
        self.phones.append(phone)
    
    def delete_phone(self, index):
        self.phones.pop(index)
    
    def edit_phone(self, index, phone: Phone):
        self.phones[index] = phone
    
        
    

class AdressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name] = record


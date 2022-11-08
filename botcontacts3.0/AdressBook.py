from collections import UserDict

class Field:
    def __init__(self, value: str):
        self.value = value

class Name(Field):
    pass

class Phone(Field):
    pass

class Record:
    
    def __init__(self, name: str, phone=None):
        self.name = Name(name)
        self.phones = []
        
    def get_info(self):
        phones_info = [phone.value for phone in self.phones]
        return f'{self.name.value} : {", ".join(phones_info)}'
            
    
    def add_phone(self, phone: str):
        self.phones.append(Phone(phone))
    
    def delete_phone(self, phone: str):
        for record_phone in self.phones:
            if record_phone.value == phone:
                self.phones.remove(record_phone)
                return True
        return False
    
    def change_phone(self, phones):
        for phone in phones:
            if not self.delete_phone(phone):
                self.add_phone(phone)
    
        
    

class AdressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def get_all_record(self):
        return self.data

    def has_record(self, name):
        return bool(self.data.get(name))

    def get_record(self, name) -> Record:
        return self.data.get(name)

    def remove_record(self, name):
        del self.data[name]

    def search(self, value):
        if self.has_record(value):
            return self.get_record(value)

        for record in self.get_all_record().values():
            for phone in record.phones:
                if phone.value == value:
                    return record

        raise ValueError("Contact with this value does not exist.")
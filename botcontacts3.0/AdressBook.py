from collections import UserDict
from datetime import datetime
import pickle

class Field:
    def __init__(self, value: str):
        self._value = None
        self.value = value
    
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, value):
        self._value = value
        
    
class Name(Field):
    
    @Field.value.setter
    def value(self, name: str):
        if name.isnumeric():
            raise ValueError('Wrong name')
        self._value = name
        
class Phone(Field):
    
        
    @Field.value.setter
    def value(self, phone: str):
        if not phone.isnumeric():
            raise ValueError('Wrong phones')
        format_phone = self.format_phone_number(phone)
        if format_phone:
            self._value = format_phone
        
    @staticmethod
    def format_phone_number(phone: str):
        if len(phone) == 10:
            return f'+38{phone}'
        elif len(phone) == 12:
            return f'+{phone}'
        else:
            raise ValueError('Wrong phones')    
    

class Birthday(Field):
    
    @Field.value.setter
    def value(self, birthday: str):
        current_date = datetime.now().date()
        birthday_date = datetime.strptime(birthday, '%Y-%m-%d').date()
        if birthday_date > current_date:
            raise ValueError("Your contact havent born yet")
        self._value = birthday
        
class Record:
    
    def __init__(self, name: str):
        self.name = Name(name)
        self.phones = []
        self.birthday = None
        
    def get_info(self):
        birthday_info = ''
        phones_info = [phone.value for phone in self.phones]
        
        if self.birthday:
            birthday_info = f' Birthday: {self.birthday.value}'
            
        return f'{self.name.value} : {", ".join(phones_info)}{birthday_info}'
            
    def day_to_bithday(self):
        if not self.birthday:
            raise ValueError('This contact havent birthday date')
        
        current_date = datetime.now().date()
        
        birthday_date = datetime.strptime(self.birthday.value, '%Y-%m-%d').date()
        this_year_birthday = birthday_date.replace(year=current_date.year)
        
        if this_year_birthday < current_date:
           this_year_birthday = this_year_birthday.replace(year=current_date.year + 1)
            
        return (this_year_birthday - current_date).days
        
    def add_phone(self, phone: str):
        self.phones.append(Phone(phone))
        
    def add_birthday(self, date: str):
        self.birthday = Birthday(date)
    
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
    def __init__(self):
        super().__init__()
        self.load_from_file()
        
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
    
    
    def iterator(self, count=3):
        result = []
        
        for contact in self.data.values():
            result.append(contact)
            if len(result) == count:
                yield result
                result = []
        
        if result:
            yield result
            
    def save_to_file(self):
        with open('AdressBook.bin', 'wb') as fw:
            pickle.dump(self.data, fw)
    
    def load_from_file(self):
        try:
            with open('AdressBook.bin', 'rb') as fr:
                self.data = pickle.load(fr)
        except FileNotFoundError:
            pass
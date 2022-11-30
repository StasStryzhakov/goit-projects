from abc import abstractmethod, ABC


class Message(ABC):
    
    @abstractmethod
    def get_message():
        pass
    

class HelpMessage(Message):
    
    @staticmethod
    def get_message():
        return '''Command to execute: 
>>> hello
>>> help - show commands list
>>> add - add new contact in storage Example: add "name (only letters without spaces)" "phone number (only digits without spaces)"
>>> change - change existing contact Example: chnage "exist contact name (only letters without spaces)" "new phone number (only digits without spaces)"
>>> phone - show exist contact name and phone
>>> show all - show all existing contacts
>>> delete phone - remove entered phone from contact Example: delete phone "name (only letters without spaces)" "phone number (only digits without spaces)"
>>> delete - remove contact Example: delete "name (only letters without spaces)" 
>>> good bye/close/exit - bye bye
>>> birthday - add birthday date to the contact Example: bithday name date(yyyy-mm-dd)
>>> days to birthday - show how much days left to the contact birthday Example: days to birthday name\n'''

class GreetingMessage(Message):
    
    @staticmethod
    def get_message():
        return 'How can I help you?'
    
class StopMessage(Message):
    
    @staticmethod
    def get_message():
        return 'Good bye!'
    
class AddContactMessage(Message):
    
    @staticmethod
    def get_message(name):
        return f'contact {name} was added'

class ChangeContacPhonetMessage(Message):
    
    @staticmethod
    def get_message(name):
        return f'contact {name} was updated'   
     
class DeletePhoneMessage(Message):
    
    @staticmethod
    def get_message(flag, name, phone):
        if flag:
            return f'Phone {phone} for {name} contact deleted.'
        return f'{name} contact does not have this number'
    
class DeleteContactMessage(Message):
    
    @staticmethod
    def get_message(name):
        return f'Contact {name} was deleted' 
    
class AddContactBirthdayMessage(Message):
    
    @staticmethod
    def get_message(name, birthday):
        return f'For {name} you add Birthday {birthday}' 
    
class DaysToBirthdayMessage(Message):
    
    @staticmethod
    def get_message(name, days):
        return f'{days} left for the contact birthday {name}'       



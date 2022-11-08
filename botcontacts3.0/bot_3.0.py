from AdressBook import AdressBook, Record

CONTACTS = AdressBook()

def get_help():
    return '''Command to execute: 
>>> hello
>>> help - show commands list
>>> add - add new contact in storage Example: add "name (only letters without spaces)" "phone number (only digits without spaces)"
>>> change - change existing contact Example: chnage "exist contact name (only letters without spaces)" "new phone number (only digits without spaces)"
>>> phone - show exist contact name and phone
>>> show all - show all existing contacts
>>> delete phone - remove entered phone from contact Example: delete phone "name (only letters without spaces)" "phone number (only digits without spaces)"
>>> delete - remove contact Example: delete "name (only letters without spaces)" 
>>> good bye/close/exit - bye bye\n'''

def input_error(func):
    def inner(*args, **kwargs):
        try:           
            return func(*args, **kwargs)
                        
        except KeyError:
            return 'This contact doesnt exist, please try again.'
        except ValueError as exception:
            return exception.args[0]
        except IndexError:
            return 'This contac cannot be added, it exists already'
        except TypeError:
            return 'Unknown command or parametrs, please try again.'
                       
    return inner    
    

def greeting():
    return 'How can I help you?'

def stop_bot():
    return 'Good bye!'

def add_contact(data):
    
    name, phones = get_data_from_user(data)
    
    if name in CONTACTS:
        raise ValueError('This contact already exist.')
    
    record = Record(name)
    
    for phone in phones:
        record.add_phone(phone)
        
    CONTACTS.add_record(record)
    
    return f'contact {name} was added'


def change_contact(data):
    
    name, phones = get_data_from_user(data)
    record = CONTACTS[name]
    record.change_phone(phones)
    
    return 'Contact was updated'


def show_contact_phone(data: str):
    return CONTACTS.search(data.strip()).get_info()
    
    


def show_all_contacts():
    result = [record.get_info() for record in CONTACTS.values()]
    return '\n'.join(result)
    

def del_phone(data):
    name, phone = data.strip().split(' ')

    record = CONTACTS[name]
    if record.delete_phone(phone):
        return f'Phone {phone} for {name} contact deleted.'
    return f'{name} contact does not have this number'

def del_contact(data):
    CONTACTS.remove_record(data.strip())
    return 'Contact was deleted'

COMMANDS = {'hello': greeting,
            'help': get_help,
            'add': add_contact,
            'change': change_contact,
            'phone': show_contact_phone,
            'show all': show_all_contacts,
            'good bye': stop_bot,
            'close': stop_bot,
            'exit': stop_bot,
            'delete phone': del_phone,
            'delete': del_contact}

def break_func():
    return 'Wrong enter'

def get_data_from_user(data: str):
    name, *phones = data.lower().strip().split(' ')
    
    if name.isnumeric():
        raise ValueError('Wrong name')
    
    for phone in phones:
        if not phone.isnumeric():
            raise ValueError('Wrong phones')
    return name, phones

def get_command(command):
    return COMMANDS.get(command, break_func)

@input_error
def get_user_request(user_input: str):
    command = ''
    data = ''
    
    for key in COMMANDS:
        if user_input.strip().lower().startswith(key):
            command = key
            data = user_input[len(key):]
            break
        
    if data:
        return get_command(command)(data)
    return get_command(command)()


  
    

def main():
    print(get_help())
    while True:
        
        user_request = input('Wait for your command master: ')
        result = get_user_request(user_request)
        print(result)
        
        if result == 'Good bye!':
            break
        
        
                
        



if __name__ == '__main__':
    main()
import re


CONTACTS = dict()

def get_help(parameters=None):
    print('''Command to execute: 
>>> hello
>>> help - show commands list
>>> add - add new contact in storage Example: add "name (only letters without spaces)" "phone number (only digits without spaces)"
>>> change - change existing contact Example: chnage "exist contact name (only letters without spaces)" "new phone number (only digits without spaces)"
>>> phone - show exist contact name and phone
>>> show_all - show all existing contacts
>>> good_bye/close/exit - bye bye\n''')

def input_error(func):
    def inner(string: str):
        try:
            if string in ('good_bye', 'close','exit'):
                func(string)
                return True
            
            parameters_list = string.lower().strip().split()
            if len(parameters_list) == 1:
                func(*parameters_list)
            elif 1 < len(parameters_list) <= 3:
                command, *params = parameters_list
                func(command, parameters=params)

            
        except KeyError:
            print('This contact doesnt exist, please try again.')
        except ValueError:
            print('Unknown command or parametrs, please try again.')
        except IndexError:
            print('index_error') 
        except TypeError:
            print('Wrong Parameters, please try again.')            
                       
    return inner    
    

def greeting(parameters=None):
    print('How can I help you?')

def stop_bot(parameters=None):
    print('Good bye!')

def add_contact(parameters=None, contacts=CONTACTS):
    contact_info = parameters
    if len(contact_info) == 2 and contact_info[0] not in contacts:
        contacts[contact_info[0]] = contact_info[1]    
    else:
        raise ValueError


def change_contact(parameters=None, contacts=CONTACTS):
    contact_info = parameters
    if len(contact_info) == 2:
        if contact_info[0] in contacts:
            contacts[contact_info[0]] = contact_info[1]
        else:
            raise KeyError
    else:
        raise ValueError


def show_contact_phone(parameters=None, contacts=CONTACTS):
    contact_info = parameters
    if len(contact_info) == 1:
        print(contacts.get(*contact_info))
    else:
        raise KeyError
    


def show_all_contacts(parameters=None, contacts=CONTACTS):
    for name, phone in contacts.items():
        print(name, phone)

COMMANDS = {'hello': greeting,
            'help': get_help,
            'add': add_contact,
            'change': change_contact,
            'phone': show_contact_phone,
            'show_all': show_all_contacts,
            'good_bye': stop_bot,
            'close': stop_bot,
            'exit': stop_bot}

@input_error
def get_command(command: str, parameters=None, commands=COMMANDS):
    commands.get(command)(parameters)
  
    

def main():
    get_help()
    while True:
        if get_command(input('Wait for your command master: ')):
            break
        



if __name__ == '__main__':
    main()
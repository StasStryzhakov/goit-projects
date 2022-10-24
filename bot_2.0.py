CONTACTS = dict()

def get_help():
    return '''Command to execute: 
>>> hello
>>> help - show commands list
>>> add - add new contact in storage Example: add "name (only letters without spaces)" "phone number (only digits without spaces)"
>>> change - change existing contact Example: chnage "exist contact name (only letters without spaces)" "new phone number (only digits without spaces)"
>>> phone - show exist contact name and phone
>>> show_all - show all existing contacts
>>> good_bye/close/exit - bye bye\n'''

def input_error(func):
    def inner(*args, **kwargs):
        try:           
            return func(*args, **kwargs)
                        
        except KeyError:
            return 'This contact doesnt exist, please try again.'
        except ValueError:
            return 'Unknown command or parametrs, please try again.'
        except IndexError:
            return 'This contac cannot be added, it exists already'
        except TypeError:
            return 'Unknown command or parametrs, please try again.'
                       
    return inner    
    

def greeting():
    return 'How can I help you?'

def stop_bot():
    return 'Good bye!'

def add_contact(parameters=None, contacts=CONTACTS):
    contact_info = parameters
    if len(contact_info) == 2:
        if contact_info[0] not in contacts:
            contacts[contact_info[0]] = contact_info[1]
        else:
            raise IndexError
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
        return (contacts.get(*contact_info))
    else:
        raise KeyError
    


def show_all_contacts(parameters=None, contacts=CONTACTS):
    return [(name, phone) for name, phone in contacts.items()]

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
    return commands.get(command)(parameters) if parameters else commands.get(command)()
  
    

def main():
    print(get_help())
    while True:
        string = input('Wait for your command master: ')
        parameters_list = string.lower().strip().split()
      
        if len(parameters_list) == 1:
            result = get_command(*parameters_list)
            if result:
                if type(result) == str:
                    print(result)
                    if result == 'Good bye!':
                        break
                else:
                    for el in result:
                        print(el[0], el[1])
                        
        elif len(parameters_list) > 1:
            command, *params = parameters_list
            result = get_command(command, parameters=params)
            if result:
                print(result)
        elif not string:
            print('I still wait for your command')
        
                
        



if __name__ == '__main__':
    main()
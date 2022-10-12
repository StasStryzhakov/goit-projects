from datetime import datetime
import random


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
    if emploee_birthdays:
        for day, birthday_boy in emploee_birthdays.items():
            print(f'{day}: {", ".join(birthday_boy)}')
    else:
        print('No birthdays next week')
        
def main():
    get_birthdays_per_week(employees_list)
    
    
if __name__ == '__main__':
    main()   
import sqlite3
import sys



def task_run(file):
    with open(file) as f:
        sql = f.read()

    with sqlite3.connect('university.db') as connect:
        cursor = connect.cursor()
        cursor.execute(sql)
        return cursor.fetchall()


def main():
    
    while True:
        task_number = int(input("Input task number from 1-10: "))
        if task_number == 0:
            sys.exit()
        result = task_run(f'task_{task_number}.sql')
        print(result)


if __name__ == '__main__':
    try:
        exit(main())
    except KeyboardInterrupt:
        exit()
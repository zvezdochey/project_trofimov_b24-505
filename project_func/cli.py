import prompt


def welcome():
    commands = '<command> exit - выйти из программы\n<command> help - справочная информация'
    command = prompt.string('Введите команду: ')
    while command != 'exit':
        if command == 'help':
            print(commands)
        else:
            print('Такая команда отсутствует(')
        command = prompt.string('Введите команду: ')
    print('Си ю сун!')
    return 0

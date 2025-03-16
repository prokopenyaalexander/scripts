import string
import random

letters = [letter for letter in string.ascii_uppercase + string.ascii_lowercase]
numbers = [number for number in range(10)]
symbols = [number for number in list('!@#$%^&*()')]

def generate_password(letters, numbers, symbols, cnt=None):
    password = ''
    all_characters = letters + numbers + symbols
    while cnt !=0:
        choice = random.choice(all_characters)
        password += str(choice)
        cnt -= 1
    return password
    

flag = True
while flag:
    print('Меню')
    print('1 - Ввести длину пароля')
    print('0 - Выход')
    ans = input()
    if ans.isdigit():
        ans = int(ans)
        if ans == 1:
            print('Введите длину пароля')
            cnt = int(input())
            print(generate_password(letters, numbers, symbols, cnt))
            flag = False
        elif ans == 0:
            break
        else:
            if ans > 1 or ans < 0 :
                print('Неверный ввод, повторите попытку')
                print('1 - Ввести длину пароля')
                print('0 - Выход')
    else:
            print('Неверный ввод, ввели букву, повторите попытку')
            print('1 - Ввести длину пароля')
            print('0 - Выход')

    if flag == False:
        break








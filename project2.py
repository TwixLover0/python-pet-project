#нужно угадать код-слово которое является паролем 
for i in range(3):
    password=input('Введи свой пароль :')
    if password != 'слон':
        continue
    break
print('Добро пожаловать! User#1')
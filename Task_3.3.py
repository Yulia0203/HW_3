# Задача 3. Создайте скрипт бота, который находит ответы на фразы по ключу в словаре. Бот должен, как минимум, отвечать на фразы «привет», «как тебя зовут». Если фраза ему неизвестна, он выводит соответствующую фразу.
# «как тебя зовут?» –> меня зовут Анатолий

dictionary = \
    {

        'Привет' : 'Добрый день',
        'Как тебя зовут?' : 'Меня зовут Анатолий',
        'Какая сегодня погода?': 'Сегодня пасмурно, надо взять зонт',
        'выход': 'Хорошего дня'
    }

isStart = True
while isStart:
    answer = input("Я: ")
    if answer == "Выход" :
        isStart = not isStart
    if answer in dictionary.keys():
        print('Бот:', dictionary[answer])
    else:
        print('Бот: неизвестная команда')

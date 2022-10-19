# Задача 2. В файле находятся названия фруктов. Выведите все фрукты, названия которых начинаются на заданную букву.
# а –> абрикос, авокадо, апельсин, айва.

with open('dict.txt', encoding='utf-8') as data:
    text = data.read().split()
    print(text)
    letter = 'б'
    for world in text:
        if world[0].lower() == letter.lower():
            print(world)
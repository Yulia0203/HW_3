# Задача 1. Создайте файл. Запишите в него N первых элементов последовательности Фибоначчи.
# 6 –> 1 1 2 3 5 8

def main():
    n = int(input("Введите число N: "))
    create_sequence(n)

def create_sequence(n):
    firstElement = 0 
    secondElement = 1
    with open('fibonacci.txt', 'w') as ouf:
        ouf.write(f'fibonacci elements of {n}: \n')
        for i in range(1, n + 1):
            ouf.write(str(i) + ':\t' + str(firstElement) + '\n')
            firstElement, secondElement = secondElement, firstElement + secondElement

if __name__ == '__main__':
    main()
"""
import pickle
import os

storage_filename = "storage.pickle"

list = ['спать', 'Машина', 'Мотоцикл', 'Еще что-нибудь', 'тд']

if not os.path.exists(storage_filename): # Если файла не существует
    with open(storage_filename, "wb") as f: # То создаем его
        pickle.dump(list, f) # Сохрняя в него наш список
else: # Если же существует
    with open(storage_filename, "rb") as f:
        list = pickle.load(f) # То загружаем из него список

num = input('Введите слово:')
list.append(num)
for i in list:
    print(i)

with open(storage_filename, "wb") as f:
    pickle.dump(list, f) # Сохраняем измененный список в файл




entered_list = input("Введите список чисел, разделенных пробелом: ").split()

num_list = [int(i) for i in entered_list]
print("Список чисел: ", num_list)

x, y = (float(input("Enter nums: "))
b=(3+x*y for x, y) 
print(b)


entered_list = input("Введите список чисел, разделенных пробелом: ").split()
print("Введенный список:", entered_list)

num_list = list(map(int, entered_list))
print("Список чисел: ", num_list)
print("Сумма списка:", sum(num_list))
"""
###################################
print(f"Введите три значения подряд через пробел: \n",)
while True:
    try:

        a, b, c = map(float, input().split())
        d = a * b / c
        print(round(d, 2))
    except ValueError:
        print('\tНЕ ПРАВИЛЬНО!\n\n','ВВЕДИТЕ ПОВТОРНО:\n')
        continue
    else:
        break
"""
def func_1():
    print(f"Введите три значения подряд через пробел: \n",)
    a, b, c = map(float, input().split())
    d = a * b / c
    print(round(d, 2))

func_1()
"""
###################################
    
import sys
print(f"Введите два значения подряд через пробел: \n",)
a, b = map(int, input().split())
c = a + b
sys.stdout.write("\x1b[1A")
sys.stdout.write('{} {} {}'.format(a, b, c))

#a, b, c = map(int, input().split())
#for a,b,c in input():
#    print(a+b+c)
    

#
#print(g)
#lst = list(map(int, input().split()))
################################
print(f"Введите три целочисленных значения подряд: \n",)
list_data = [float(v) * float(z) /float(q) for v, z, q in input().split()]
#print(f"Введите значения подряд:{list_data} ")
print(list_data,)


list_data = input().split()
int_lst = []
for element in list_data:
    if element.isdigit():
        int_lst.append(int(element))
    else:
        print(f'{element} - не является числом! ')
        print('Ошибка формирования списка чисел!')
        exit()
print(f'Ваш список чисел:', int_lst)

#################################
while True:
    try:
        a = int(input("Введите целое число: "))
    except:
        print("Вы ввели не целое число, ошибка")
        continue
    break

a, b = 9, 10
print(a & b)  # line 1
print(a and b)  # line 2

# Операции над двумя числами
def sum(a, b):
    return a + b
def sub(a, b):
    return a - b
def mult(a, b):
    return a * b
def div(a, b):
    return a / b

def main():
    while True:
        try:
            #Вводим числа
            a = float(input("Введите первое число: "))
            b = float(input("Введите второе число: "))
            c = int(input("Номер операции:\n1) +\n2) -\n3) *\n4) /\n"))
        except:
            print("Нужно ввести число, попробуйте ещё раз ...\n")
            continue # Повторяем ввод, если введено не число
        break # Выходим из цикла, если числа введены правильно
    # Применяем нужную операцию в зависимости от ввода
    cond = {1 : sum(a, b),
            2 : sub(a, b),
            3 : mult(a, b),
            4 : div(a, b)}
    # Выводим результат операции
    print(cond[c])

if __name__ == "__main__":
    main()
#######
print(list(map(int, input('Введите числа, из которых будет состоять список: \n').split())))

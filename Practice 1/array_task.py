def task_1():
    array = create_array()
    position = search_for_position(array)
    print(f'Result = {position}')

# Считывание числа у пользователя
def read_number():
    number = input()
    try:
        return float(number)
    except:
        print("Ошибка. Введи число")
        return read_number()

# Создание массива
def create_array():
    print("Количество элементов в массиве равно ?")
    n = read_number()
    array = []
    for i in range(int(n)):
        print(f'{i}. = ')
        number = read_number()
        array.append(number)
    return array

# Поиск позиции наименьшего по модулю отрицательного элемента массива
def search_for_position(array):
    filtered_array = [(abs(array[i]), i) for i in range(len(array)) if array[i] < 0]
    if len(filtered_array) == 0:
        return -1
    minimum = filtered_array[0][0]
    position = filtered_array[0][1]
    for i in range(len(filtered_array)):
        value = filtered_array[i][0]
        index = filtered_array[i][1]
        if value < minimum:
            minimum = value
            position = index
    return position
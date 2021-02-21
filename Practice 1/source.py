def main():
    array = create_array()
    search_for_position(array)


# Считывание числа у пользователя
def read_number():
    number = input()
    try:
        return float(number)
    except:
        print("Ошибка. Введи число")
        return read_number()


def create_array():
    print("Количество элементов в массиве равно ?")
    n = read_number()
    array = []
    for i in range(int(n)):
        print(f'{i}. = ')
        number = read_number()
        array.append(number)
    return array


def search_for_position(array):
    filtered_array = [abs(i) for i in range(len(array)) if i < 0]
    if len(filtered_array) == 0:
        return -1
    minimum = filtered_array[0]
    position = 0
    for i in range(len(filtered_array)):
        if filtered_array[i] < minimum:
            minimum = filtered_array[i]
            position = i
    return position


main()

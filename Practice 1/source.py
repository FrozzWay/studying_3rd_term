def main():
    print("Количество элементов в массиве равно ?")
    n = input()
    if not n.isnumeric():
        print("N должно быть число")
        main()
        return
    array = []
    for i in range(int(n)):
        print(f'{i}. = ')
        array[i].append(int(input()))


main()

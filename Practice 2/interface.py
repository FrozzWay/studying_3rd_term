from source import collection

collection.fill()
collection.output(True)

print("\n1. Поиск\n2. Сортировка")

do = input()

if do == "1":

    print("Критерий?\n1. surname\n2. reg_number\n3. up_to")
    criteria = input()
    print("Значение:")
    value = input()

    if criteria == "1":
        collection.search("surname", value)
    elif criteria == "2":
        collection.search("reg_number", value)
    elif criteria == "3":
        collection.search("up_to", value)

if do == "2":
    print("Критерий?\n1. surname\n2. reg_number\n3. up_to")
    criteria = input()

    if criteria == "1":
        collection.sort("surname")
    elif criteria == "2":
        collection.sort("reg_number")
    elif criteria == "3":
        collection.sort("up_to")
    collection.output(False)
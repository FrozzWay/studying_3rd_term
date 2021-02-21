def task_2():
    print("String 1: ")
    string1 = input().strip()
    print("String 2: ")
    string2 = input().strip()
    if string1 > string2:
        print("string1 > string2")
    elif string1 == string2:
        print("string1 == string2")
    else:
        print("string1 < string2")
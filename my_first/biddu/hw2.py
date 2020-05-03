def adding_1(dict1):
    dict1.update({3: 30})
    print(dict1)


def cat_2():
    newdict1 = {**dict1, **dict2, **dict3}
    print("The dictionary has been updated")
    print(newdict1)


def check_3(check):
    if check in dict1:
        print(check, "is in the dictionary")
    else:
        print(check, "isn't in the dictionary")


def iterate_4(dict1):
    for x in dict1:
        print(x, "is the key for")
        print(dict1[x])


def square_5():
    for i in range(1, 10):
        a = i
        square.update({a, a ^ 2})
    print(square)


def Sum_6(newDict):
    sum = 0
    for i in newDict:
        sum = sum + newDict[i]

    print("Sum :", sum)


square = {}

dict1 = {
    1: 10,
    2: 20
}

dict2 = {
    3: 30,
    4: 40
}
dict3 = {
    5: 50,
    6: 60
}

newDict = {'a': 100, 'b': 200, 'c': 300}

Sum_6(newDict)
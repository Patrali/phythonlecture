def play1():
    for i in range(0, 10):
        sum = i + 2
        print("sum1:", sum)



def play2():
    for i in range(0, 10):
        sum = i + 2
        return sum
#i = 0, sum = 2 , return 2

def play3():
    for i in range(0, 10):
        sum = i + 2
    return sum


def play4():
    for i in range(0, 10, 2):
        sum = i + 2
        return sum


def play5():
    for i in range(0, 10):
        sum = i + 2
    return sum

#play1()
#print(" ans to play2 : " + str(play2()))
print(" ans to play3 : " + str(play3()))
#print(" ans to play4 : " + str(play4()))
#print(" ans to play5 : " + str(play5()))



print("This line will be printed.")



def my_print(fname):
  print(fname + " Refsnes")

def increase_by_two(mylist):
    for i in range(0, 10, 2):
        print("list 1:", i)

    #(L[start:stop:step]):
    for i in mylist[::2]:
        print("list 2 : ", i)
    # prints 1 3 5 7 9

    for i in mylist[1::2]:
        print("list 3 : ", i)
    # prints 2 4 6 8 10

#=================THIS SECTION TO UNDERSTAND LOGIC FLOW===============================
def play1():
    for i in range(0, 10):
        sum = i + 2
        print("sum1:", sum)


def play2():
    for i in range(0, 10):
        sum = i + 2
        return sum


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

#=================END : THIS SECTION TO UNDERSTAND LOGIC FLOW===============================
def handleFile():
    f = open("guru99.txt", "w+")
    for i in range(10):
        f.write("This is line %d\n" % (i + 1))
    f.close()

    print("----------------read full content-----------------------")
    f = open("guru99.txt", "r")
    if f.mode == 'r':
        contents = f.read()
        print("1st : " +contents)
    f.close()
    #read each line
    print("----------------read each line-----------------------")
    f = open("guru99.txt", "r")
    fl =f.readlines()
    for x in fl:
        print( "2nd : " + x)

    f.close()
#======= Find pairs to sum 9 =======================
#Biddu's code
def sumcheck(list1):
    for i in range(0,len(list1)):
        print("Comparing",list1[i],"to other terms")
        for j in range(i+1,len(list1)):
            print(list1)
            if(list1[i] + list1[j] == 9):
                print("The numbers",list1[i],"and",list1[j],"add to 9")
    return(list1)

#Souvik's code
list1 = [5,2,7,4,3,8,1]
def find9(list):
    for i in range(len(list)):
        for j in range(i+1, len(list)):
            if list[i] + list[j] == 9:
                print("[",list[i],",",list[j],"]")


find9(list1)
#======= END : Find pairs to sum 9 =======================


#my_print("Patrali")
#mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#increase_by_two(mylist)
#handleFile()
#sumcheck([5,2,7,4,3,8,1])

#play1()
#print("sum2:", play2())
#print("sum3:", play3())



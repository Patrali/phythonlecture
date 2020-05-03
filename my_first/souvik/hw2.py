'''
1. Write a Python script to add a key to a dictionary.

Sample Dictionary : {0: 10, 1: 20}
Expected Result : {0: 10, 1: 20, 2: 30}
'''
myDict = {"hello": "world"}


def addKey(dict, key):
    myDict.update(key)
    print(myDict)


addKey(myDict, {"Python": "fun"})


3
# Iterate over key/value pairs in dict and print them
for key, value in myDict.items():
    print(key, ' : ', value)
print("-----------------------------------------")
'''
2. Write a Python script to concatenate following dictionaries to create a new one. 

Sample Dictionary :
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
'''
dic1 = {0: 1}
dic2 = {1: 2}
dic3 = {2: 3}


def createDict(dict1, dict2, dict3):
    dict1.update(dict2)
    dict1.update(dict3)
    print(dict1)


createDict(dic1, dic2, dic3)

print("-----------------------------------------")
'''
3. Write a Python script to check whether a given key already exists in a dictionary.
'''
myDict = {1 : 2,
          2 : 3,
          3 : 4}
def findKey(myDict, key, value):
    thisKey = myDict.get(key, value)
    print(thisKey)

findKey(myDict, 3, 4)

print("-----------------------------------------")
'''
4. Write a Python program to iterate over dictionaries using for loops. 
'''
myDict = {1 : 2,
          2 : 3,
          3 : 4}
def iterateOver(myDict):
    for key in myDict:
        print(key, ' : ', myDict[key])


iterateOver(myDict)

print("-----------------------------------------")
'''
5. Write a Python script to generate and print a dictionary that contains a number (between 1 and n) 
in the form (x, x*x). 
Sample Dictionary ( n = 5) :
Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
'''
def squaredDict():
    list = [1,2,3,4,5,6]
    theDict = {}
    for n in range(1,len(list)):
        theDict.update({n : n*n})
    print(theDict)
squaredDict()
print("-----------------------------------------")
'''
6. Write a Python script to print a dictionary where the keys are numbers between 1 and 15 
(both included) and the values are square of keys. 
Sample Dictionary
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
'''
def squaredDict2():
    theDict = {}
    for n in range(1,16):
        theDict.update({n : n*n})
    print(theDict)
squaredDict2()
print("-----------------------------------------")
'''
7. Write a Python program to iterate over dictionaries using for loops. 
'''

'''
8. Write a Python program to sum all the items in a dictionary. 

'''
dict2 = { 5 : 2,
          3 : 6,
          9 : 2}
def addDict(thisDict):
    sum1 = 0
    for item in thisDict:
        sum1 = sum1 + thisDict[item]
    print(sum1)
addDict(dict2)
def readFileTop2():
    fileHandle = open("wordcountsource.txt")
    dataList = fileHandle.readlines()
    wordDict = dict()
    bruh = 0
    for line in dataList:
        wordList = line.split()
        for word in wordList:
            if word in wordDict:
                wordDict[word] = wordDict[word] + 1
            else:
                wordDict[word] = 1
    from collections import Counter 
    k = Counter(wordDict)
    highestWords = k.most_common()
    for word in highestWords: 
        print(word[0]," :",word[1])  
    fileHandle.close()
readFileTop2()


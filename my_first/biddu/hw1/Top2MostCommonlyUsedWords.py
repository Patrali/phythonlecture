#Finding top 2 most common words

ordering = []


def wordCount():
    file = open("wordcountsource.txt", "r")
    d = dict()
    if file.mode == "r":

        lines = file.readlines()
        for line in lines:
            words = line.split()
            for word in words:
                if word in d:
                    d[word] = d[word] + 1
                    print(word)

                else:
                    d[word] = 1

        for key in list(d.keys()):
            print(key, ":", d[key])
            d.update({key: d[key]})
        print(d)
        new_dict = {}
        for key, value in d.items():
            if value in new_dict:
                new_dict[value].append(key)
            else:
                new_dict[value] = [key]
        file.close()
        #     print(new_dict)
        #      print(ordering)
        for i in new_dict:
            print("The words", new_dict[i], "appeared", i, "times")


wordCount()
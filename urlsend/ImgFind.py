import re

srctags = []
file = open("data1.txt", "r")
data = file.read()
file.close()
lst = data.split("|")
for i in range(len(lst)):
    list1 = lst[i].split("\"")
    for i1 in range(len(list1)):
        x = re.search("https://.*", list1[i1])
        x1 = re.match("//.*", list1[i1])
        x2 = re.search(".*svg", list1[i1])
        if (x != None and x2 == None):
            srctags.append(list1[i1])
        if (x1 != None and x2 == None):
            srctags.append("https:" + list1[i1])
file = open("data2.txt", "w+")
file.write("|".join(srctags))
file.close()

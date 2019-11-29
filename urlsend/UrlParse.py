import re

file = open("data.txt", "r")
text = file.read()
file.close()
i = 0
string = ""
cmds = []
for i in range(len(text)):
    if (text[i] == ">"):
        cmds.append(string + ">")
        string = ""
    else:
        string = string + text[i]
imgs = []
i = 0
for i in range(len(cmds)):
    if (re.search("^<img.*>$", cmds[i]) != None):
        imgs.append(cmds[i])
file = open("data1.txt", "w+")
file.write("|".join(imgs))
file.close()

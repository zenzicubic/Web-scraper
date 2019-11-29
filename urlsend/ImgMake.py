import urllib.request

file = open("data2.txt", "r")
text = file.read().split("|")
file.close()
byteslist = []
for i in range(len(text)):
    try:
        UrlDat = urllib.request.urlopen(text[i])
        bytesDat = UrlDat.read()
        byteslist.append(bytesDat)
        f = open("img/image" + str(i) + ".png",'wb+')
        f.write(bytesDat)
        f.close()
    except urllib.error.HTTPError:
        print("")

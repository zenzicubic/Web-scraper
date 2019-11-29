import urllib.request

# Reading the URL data and writing it to a file.
UrlDat = urllib.request.urlopen("https://url")
file = open("data.txt", "w+")
file.write(str(UrlDat.read()))
file.close()

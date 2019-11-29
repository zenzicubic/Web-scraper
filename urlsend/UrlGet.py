import urllib.request

# Reading the URL data and writing it to a file.
UrlDat = urllib.request.urlopen("https://www.reddit.com/r/Ooer")
file = open("data.txt", "w+")
file.write(str(UrlDat.read()))
file.close()

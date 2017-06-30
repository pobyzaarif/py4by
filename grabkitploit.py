import urllib

url = urllib.urlopen("http://www.kitploit.com/")
site = []
numMatch = []
for count, line in enumerate(url) :
    site.append(line)
    if line.startswith("<h2 class='post-title entry-title'>") :
         numMatch.append(count)

numPage = 0
for i in numMatch :
    numPage+=1
    tittle = (site[i+2]).rstrip()
    link = site[i+1]
    link = link[9:-3]
    print numPage, tittle, '=>', link

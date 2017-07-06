import urllib
import sys

url = 'http://www.kitploit.com/'

def first(url):
  urls = urllib.urlopen(url)
  site = []
  numMatch = []
  for count, line in enumerate(urls) :
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

def second(pnum):
  urls = 'http://www.kitploit.com/search?updated-max=2017-06-28T19%3A30%3A00-04%3A00&max-results=' + pnum
  return urls

if __name__ == '__main__':
  first(url)
  print '\n========================================================='
  arg = raw_input('another?  : ')
  if arg.lower() == 'y' :
    pnum = raw_input('next result max? : ')
    print '=========================================================\n'
    url = second(pnum)
    first(url)
  else :
    sys.exit(1)

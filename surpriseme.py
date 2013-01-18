#Import libraries
import urllib2,os
#beautifulSoup can be downloaded from http://www.crummy.com/software/BeautifulSoup/bs4/download/
from bs4 import BeautifulSoup

#Surprise me. This will download random image from xkcd website.
rand=urllib2.urlopen("http://dynamic.xkcd.com/random/comic/")

soup=BeautifulSoup(rand.read())

#Saving file to the current directory in which you are working.
f=open(os.getcwd()+'\xkcd_comic.png','wb')

f.write(urllib2.urlopen(soup.find_all(id="comic")[0].img['src']).read())

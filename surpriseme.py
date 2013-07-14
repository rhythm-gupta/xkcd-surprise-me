"""
Surprise me. This script will download a random image from xkcd website.

"""

import urllib2, os
from bs4 import BeautifulSoup

img_name = 'xkcd_comic.png'   #change this if you want different file name
rand = urllib2.urlopen("http://dynamic.xkcd.com/random/comic/")

soup = BeautifulSoup(rand.read())

#Saving file to the current directory in which you are working.
file_name = os.path.join(os.getcwd(), img_name)
with open(file_name, 'wb') as f:
    f.write(urllib2.urlopen(soup.find_all(id="comic")[0].img['src']).read())

***

This file downloads all the images from xkcd.

***

import urllib2,time,os
from bs4 import BeautifulSoup
for i in range(1,1163):#corrently there are 1162 images on xkcd. this number is subjected to change.
    rand=urllib2.urlopen("http://xkcd.com/"+str(i))
	soup=BeautifulSoup(rand.read())
	f=open(os.getcwd()+"\xkcd\"str(i)+'.png','wb')
	f.write(urllib2.urlopen(soup.find_all(id="comic")[0].img['src']).read())
	time.sleep(2)#I've used a timesleep of 2 seconds so that xkcd servers don't ban our ip.
	#PS: You can comment this sleep function if you want to , cuz I've downloaded their whole directory but
	#still they didn't ban my IP. ;)
	print("Downloaded image no: "+str(i))

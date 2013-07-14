"""

This file downloads all the images from xkcd.

"""

import urllib2, time, os
from bs4 import BeautifulSoup
#currently there are 1162 images on xkcd. this number is subjected to change.
image_count = 1162
url = "http://xkcd.com/"
ext = '.png'
for i in range(1,404) + range(405, image_count+1):
    i = str(i)
    data =  urllib2.urlopen(url + i)
    soup = BeautifulSoup(data.read())
    dir_name = os.path.join(os.getcwd(), "xkcd")
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    with open(os.path.join(dir_name,(i + ext)), 'wb') as f2:
        f2.write(urllib2.urlopen(soup.find_all(id="comic")[0].img['src']).read())
    time.sleep(2)#I've used a timesleep of 2 seconds so that xkcd servers don't ban our ip.
    #PS: You can comment this sleep function if you want to , cuz I've downloaded their whole directory but
    #still they didn't ban my IP. ;)
    print("Downloaded image no: "+ i)

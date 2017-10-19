#!/usr/bin/python3

import requests
import sys

import gi
gi.require_version('Notify', '0.7')
from gi.repository import Notify

def noti(tl, msg):
    Notify.init(tl)
    notification = Notify.Notification.new(msg)
    notification.show()

# add path to beautifulsoup library
sys.path.append('/usr/local/var/beautifulsoup')

# import it
from bs4 import BeautifulSoup

def miner(url, param, selection):
    alist = []
    #making the query parameter

    #getting the oage with the given param
    r = requests.get(url, param)

    soup = BeautifulSoup(r.text, 'lxml')

    #looping through iten-content elements
    for tag in soup.find_all('div', {'class':'nspArtScroll2 nspPages5'}):
        for title in tag.find_all('h4'):
        #print(tag.find("p", { "class" : "item-info" }))
            for tit in title.find_all('a'):
                #print(tit)
                alist.append(tit.contents)


    return alist
	

url = "http://theindependent.lk"
param = ''
news = miner(url, param, '')

i = 0
for new in news:
    print(new[i])
    noti(new[0],new[0]);


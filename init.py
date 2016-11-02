#!/usr/bin/python3

import requests
import sys

# add path to beautifulsoup library
sys.path.append('/usr/local/var/beautifulsoup')

# import it
from bs4 import BeautifulSoup

def miner(url, param, selections=''):
    #making the query parameter
    query = {param}

    #getting the oage with the given param
    r = requests.get(url, params=query)

    soup = BeautifulSoup(r.text, 'lxml')

    #looping through iten-content elements
    for tag in soup.find_all('div', {selections}):
        #print(tag.find("p", { "class" : "item-info" }))
        print(tag.text)
    return
	

url = "http://sinhala.theindependent.lk"
param = ''

miner(url, param, 'class:nspArtScroll1')

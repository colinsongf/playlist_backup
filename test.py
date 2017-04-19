#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup

headers={
'Referer':'http://music.163.com/',
'Host':'music.163.com',
'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0 Iceweasel/38.3.0',
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
}

play_url = 'http://music.163.com/playlist?id=30400705'
s = requests.session()
s = BeautifulSoup(s.get(play_url,headers=headers).content,'lxml')
main = s.find('ul',{'class':'f-hide'})

fp=open('result.txt','w')

for music in main.find_all('a'):
    fp.write(music.text+'\n')
    #print('{} : {}'.format(music.text,music['href']))
fp.close()


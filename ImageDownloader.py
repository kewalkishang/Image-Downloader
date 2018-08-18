import urllib.request
from bs4 import BeautifulSoup
import requests



def downloadSingle(url,path):
  urllib.request.urlretrieve(url,path)


def getImageLinks(url):
    global linkslist
    r=requests.get(url)
    soup=BeautifulSoup(r.content,'lxml')
    html=soup.prettify()
    print(html)
    links=soup.find('p')
    strl=str(links)
    print(type(strl))
    """print(g_data)"""
    linkslist=strl.splitlines();
    print(len(linkslist))
    print(linkslist[0])
    

def downloadFromImageNet():
    for ite in range(4):
        if ite!=0:
            path= r"F:\s"+str(ite)+".jpg"
            urllib.request.urlretrieve(linkslist[ite],path)
    

def getSynlist():
    global contents
    r=requests.get("http://image-net.org/synset?")
    soup=BeautifulSoup(r.content,'lxml')
    """html=soup.prettify()
    print(html)"""
    links=soup.find_all('wnid')
    strl=str(links)
    print(strl)
    
    
    

"""downloadSingle("http://farm1.static.flickr.com/64/177422189_2e53d16942.jpg",r"F:\00000007.jpg")"""


getImageLinks("http://image-net.org/api/text/imagenet.synset.geturls?wnid=n02506783")

print(linkslist[2])

downloadFromImageNet()

getSynlist()

ss = wn.synset('african_elephant.n.01')
print(ss)
offset = str(ss.offset()).zfill(8) + '-' + ss.pos()
print(offset)

import nltk
nltk.download()
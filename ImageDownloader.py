#import nltk
#nltk.download()
import urllib.request
from bs4 import BeautifulSoup
import requests
from nltk.corpus import wordnet as wn


def downloadSingle(url,path):
  urllib.request.urlretrieve(url,path)


def getImageLinks(sid):
    global linkslist
    url='http://image-net.org/api/text/imagenet.synset.geturls?wnid=n'+sid
    r=requests.get(url)
    soup=BeautifulSoup(r.content,'lxml')
    #html=soup.prettify()
    #print(html)
    links=soup.find('p')
    strl=str(links)
   # print(type(strl))
    """print(g_data)"""
    linkslist=strl.splitlines();
    print(len(linkslist))
    print(linkslist[0])
    

def downloadFromImageNet():
    for ite in range(4):
        if ite!=0:
            path= r"F:\s"+str(ite)+".jpg"
            urllib.request.urlretrieve(linkslist[ite],path)
    
    
def getSynsetId(his):
    name= his+'.n.01'
    try:
         ss = wn.synset(name)
         Synid = str(ss.offset()).zfill(8) + '-' + ss.pos()
         print(Synid)
    except:
        print("This is an error message!")
        Synid="0000-n"
    #print(ss)
   
    return Synid
    
    

"""downloadSingle("http://farm1.static.flickr.com/64/177422189_2e53d16942.jpg",r"F:\00000007.jpg")"""


#getImageLinks("http://image-net.org/api/text/imagenet.synset.geturls?wnid=n02506783")

#downloadFromImageNet()

#getSynlist()

#syn = getSynsetId("gog")

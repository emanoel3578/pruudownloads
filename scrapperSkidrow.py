from csv import reader
from urllib import request
from urllib.request import Request,urlopen
from bs4 import BeautifulSoup as soup
from bs4.element import ContentMetaAttributeValue
import json
import sys

i = 1
linksDict = {}
while i < 4:
    currentPageUrl = "https://www.skidrowreloaded.com/page/" + str(i) + "/"
    headers1 = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36 OPR/77.0.4054.275"
    }
    req1 = Request(currentPageUrl, headers=headers1)
    webpage1 = urlopen(req1).read()

    page_soup1 = soup(webpage1, "html.parser")
    containers1 = page_soup1.findAll("div", {"class":"post"})

    for container in containers1:
        linkcontainer= container.h2.a["href"]
        
        my_url = linkcontainer
        headers2 = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36 OPR/77.0.4054.275"
        }
        req2 = Request(my_url, headers=headers2)
        webpage2 = urlopen(req2).read()

        page_soup2 = soup(webpage2, "html.parser")
        idTabsVerifier = page_soup2.find("div", {"class" : "wordpress-post-tabs"})

        divid = idTabsVerifier.div["id"].replace("_","-") + "-0"
        
        containerTitleandLinks = page_soup2.find("div", {"id" : divid})
        
        sizeGameArrays = containerTitleandLinks.findChildren()[9].text.partition('\n')
        
        textcontainer = (containerTitleandLinks.findChildren()[2].text).partition('\n')[0][7:]

        listLinks = []
        for a in containerTitleandLinks.find_all("a", href=True):
            if "skidrow" not in a["href"]:
                listLinks.append(a["href"])


        #Getting the providers link
        providerLinks = ""
        if "Size" not in sizeGameArrays[2].partition('\n')[0]:
            currentGameSize = "| 0 GB"
        else:
            currentGameSize = "| " + sizeGameArrays[2].partition('\n')[0][6:]
            

        for item in listLinks[2:]:
            # print(item)
            if "zippyshare" in item:
                providerLinks = providerLinks + "|" + item
            elif "mediafire" in item:
                providerLinks = providerLinks + "|" + item
            elif "bowfile" in item:
                providerLinks = providerLinks + "|" + item
            elif "mega.nz" in item:
                providerLinks = providerLinks + "|" + item
            elif "magnet" in item:
                providerLinks = providerLinks + "|" + item

            linksDict[textcontainer] = providerLinks[1:] + currentGameSize

        # print(linksDict)
    i = i + 1
    print("Page:" + str(i))


sys.stdout = open("declare.js", "w")
jsonObjc = json.dumps(linksDict)
print("export var jsonstr = {}".format(jsonObjc))







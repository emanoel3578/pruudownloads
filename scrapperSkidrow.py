from csv import reader
from urllib import request
from urllib.request import Request,urlopen
from bs4 import BeautifulSoup as soup
from bs4.element import ContentMetaAttributeValue
import json
import sys

with open("titles.csv", "r", encoding="utf-8") as f:
    with open("titlesAndDownloadLink.csv", "w", encoding="utf-8") as w:
        first_url = "https://www.skidrowreloaded.com"

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36 OPR/77.0.4054.275"
        }

        reqfirst = Request(first_url, headers=headers)
        webpagefirst = urlopen(reqfirst).read()

        page_soup = soup(webpagefirst, "html.parser")
        containers = page_soup.findAll("div", {"class":"post"})
        csv_reader = reader(f)

        lastpageFind = page_soup.findAll("div", {"class":"wp-pagenavi"})
        lastpageValue = lastpageFind[0].span.text
        lastpage = int(lastpageValue[-5:].replace(",",""))

        w.write("PAGE,TITLE,LINK,DOWNLOADLINKS" + "\n")

        for row in csv_reader:
            if row[0] == "PAGE":
                continue

        i = 2
        while i != lastpage:
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
                
                currentLinkGame = linkcontainer
                my_url = currentLinkGame
                headers2 = {
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36 OPR/77.0.4054.275"
                }
                req2 = Request(my_url, headers=headers2)
                webpage2 = urlopen(req2).read()

                page_soup2 = soup(webpage2, "html.parser")
                containersLinks = page_soup2.find_all("a", href=True)

                listLinks = []
                counter = 0
                for link in containersLinks:
                    if "skidrow" not in link["href"]:
                        listLinks.append(link["href"])

                #Getting the providers link
                providerLinks = ""
                for item in listLinks[2:]: 
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

                linksDict = {}
                for container in containers:
                    textcontainer = container.h2.a.text
                    linksDict[textcontainer] = providerLinks[1:]

                row.append(providerLinks[1:])
                listToStr = (','.join([str(elem) for elem in row]))
                print(linksDict)
                i = i + 1


        sys.stdout = open("declare.js", "w")
        jsonObjc = json.dumps(linksDict)
        print("export var jsonstr = {}".format(jsonObjc))

        # Escrever links atulizados no titlesedownloads.csv
        # w.write(listToStr + "\n")






from csv import reader
from urllib import request
from urllib.request import Request,urlopen
from bs4 import BeautifulSoup as soup
from bs4.element import ContentMetaAttributeValue

with open("titles.csv", "r", encoding="utf-8") as f:
    with open("titlesAndDownloadLink.csv", "w", encoding="utf-8") as w:
        first_url = "https://www.skidrowreloaded.com"

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36 OPR/77.0.4054.275"
        }

        reqfirst = Request(first_url, headers=headers)
        webpagefirst = urlopen(reqfirst).read()

        page_soup = soup(webpagefirst, "html.parser")
        firstPage = page_soup.findAll("div", {"class":"post"})
        csv_reader = reader(f)

        w.write("PAGE,TITLE,LINK,DOWNLOADLINKS" + "\n")

        for row in csv_reader:
            if row[0] == "PAGE":
                continue
            print(row[1])
            with open("titles.csv", "w", encoding="utf-8") as r:
                lines = f.readlines()
                for item in firstPage:
                    if item.a.text != row[1]:
                        textcontainer = item.a.text
                        linkcontainer = item.a["href"]

                        lines[1] = "1" + "," + textcontainer + "," + linkcontainer + "\n"
                        
                        r.writelines(lines)

            
            #currentLinkGame = row[2]
            #print(currentLinkGame)
            # my_url = currentLinkGame
            # headers = {
            #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36 OPR/77.0.4054.275"
            # }
            # req = Request(my_url, headers=headers)
            # webpage = urlopen(req).read()

            # page_soup = soup(webpage, "html.parser")
            # containersLinks = page_soup.find_all("a", href=True)

            # listLinks = []
            # counter = 0
            # for link in containersLinks:
            #     if "skidrow" not in link["href"]:
            #         listLinks.append(link["href"])

            # #Getting the providers link
            # providerLinks = ""
            # for item in listLinks[2:]: 
            #     if "zippyshare" in item:
            #         providerLinks = providerLinks + "|" + item
            #     elif "mediafire" in item:
            #         providerLinks = providerLinks + "|" + item
            #     elif "bowfile" in item:
            #         providerLinks = providerLinks + "|" + item
            #     elif "mega.nz" in item:
            #         providerLinks = providerLinks + "|" + item
            #     elif "magnet" in item:
            #         providerLinks = providerLinks + "|" + item

            # row.append(providerLinks[1:])
            # listToStr = (','.join([str(elem) for elem in row]))
            # print(listToStr)
            # w.write(listToStr + "\n")






from urllib import request
from urllib.request import Request,urlopen
from bs4 import BeautifulSoup as soup
from bs4.element import ContentMetaAttributeValue

my_url = "https://www.skidrowreloaded.com"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36 OPR/77.0.4054.275"
}

req = Request(my_url, headers=headers)
webpage = urlopen(req).read()

page_soup = soup(webpage, "html.parser")
containers = page_soup.findAll("div", {"class":"post"})

firstpage = page_soup.findAll("div", {"class":"post"})

lastpageFind = page_soup.findAll("div", {"class":"wp-pagenavi"})
lastpageValue = lastpageFind[0].span.text
lastpage = int(lastpageValue[-5:].replace(",",""))

for item in firstpage:
    print(item.a.text)

#print(firstpage)

# with open("titles.csv", "w", encoding="utf-8") as f:
#     colums = "PAGE,TITLE,LINK\n"
#     f.write(colums)

#     for container in containers:
#         currentPageValue = "1"
#         textcontainer = container.h2.a.text
#         linkcontainer = container.h2.a["href"]

#         print(currentPageValue, textcontainer + linkcontainer + "\n")

#         f.write(currentPageValue + "," + textcontainer + "," + linkcontainer + "\n")


#     i = 2
#     while i != lastpage:
#         currentPageUrl = "https://www.skidrowreloaded.com/page/" + str(i) + "/"
#         headers1 = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36 OPR/77.0.4054.275"
#         }
#         req1 = Request(currentPageUrl, headers=headers1)
#         webpage1 = urlopen(req1).read()

#         page_soup1 = soup(webpage1, "html.parser")
#         containers1 = page_soup1.findAll("div", {"class":"post"})

#         for container in containers1:
#             currentPageValue = str(i)
#             textcontainer = container.h2.a.text
#             linkcontainer = container.h2.a["href"]

#             print(currentPageValue, textcontainer + linkcontainer + "\n")

#             f.write(currentPageValue + "," + textcontainer + "," + linkcontainer + "\n")
#         i = i + 1





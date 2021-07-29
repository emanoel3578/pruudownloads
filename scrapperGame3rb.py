from urllib import request
from urllib.request import Request,urlopen
from bs4 import BeautifulSoup as soup
from bs4.element import ContentMetaAttributeValue

my_url = "https://www.game3rb.com"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36 OPR/77.0.4054.275"
}

req = Request(my_url, headers=headers)
webpage = urlopen(req).read()

page_soup = soup(webpage, "html.parser")
containers = page_soup.findAll("h3", {"class":"g1-gamma g1-gamma-1st entry-title"})

with open("titles.csv", "w", encoding="utf-8") as f:
    colums = "TITLE,LINK\n"
    f.write(colums)
    
    for container in containers:
        textcontainer = container.a.text
        linkcontainer = container.a["href"]

        f.write(textcontainer + "," + linkcontainer + "\n")

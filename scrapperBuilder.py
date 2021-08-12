from urllib import request
from urllib.request import Request,urlopen
from bs4 import BeautifulSoup as soup
from bs4.element import ContentMetaAttributeValue
import json

# reqGOG = Request("https://www.gog.com/game/iron_harvest_deluxe_edition")
# webpageGOG = urlopen(reqGOG).read()

# page_soupGOG = soup(webpageGOG, "html.parser")
# genreGOG = page_soupGOG.find_all("div", {"class":"table--without-border"})

# if len(genreGOG) != 0:
#     developerGOG = genreGOG[-1].find_all("div", {"class" : "details__rating"})[2].div.findNext().find_all("a")[0].text
#     companyGOG = genreGOG[-1].find_all("div", {"class" : "details__rating"})[2].div.findNext().find_all("a")[1].text
#     imgHeaderGOG = page_soupGOG.find("img", {"class" : "mobile-slider__image"})["src"]
#     ratingsGOG = "Nothing"

#     # infoGOG = imgHeaderGOG + "$$" + developerGOG + "$$" + companyGOG + "$$" + ratingsGOG
#     print (imgHeaderGOG) 
# else:
#     print("Empty")


# Inicio do request para a pagina do jogo 

# testUrl = "https://www.gog.com/game/crossroads_inn_collectors_edition_limited_bundle"
# reqGOG = Request(testUrl)
# webpageGOG = urlopen(reqGOG).read()

# page_soupGOG = soup(webpageGOG, "html.parser")
# print(page_soupGOG)
# genreGOG = page_soupGOG.find_all("div", {"class":"table--without-border"})

# genreStrGOG = "|Genre:"
# releaseDateGOG = "00/00/00"
# developerGOG = genreGOG[-1].find_all("div", {"class" : "details__rating"})[2].div.findNext().find_all("a")[0].text
# companyGOG = genreGOG[-1].find_all("div", {"class" : "details__rating"})[2].div.findNext().find_all("a")[1].text
# apirul = "https://api.gog.com/v2/games/1455317728?locale=en-US"

# apiRequest = request.urlopen(apirul).read()
# apiContent = json.loads(apiRequest)
# reqstrGOG = ""

# for el in apiContent["_embedded"]["supportedOperatingSystems"][0]["systemRequirements"][0]["requirements"]:
#     reqstrGOG = reqstrGOG + (el["name"] + el["description"]) + " "

# for genre in genreGOG[-1].div.find_all("a"):
#     genreStrGOG = genreStrGOG + genre.text + "-"

# print("{} // Developer: {} // Publisher: {} // Release Date: {} // SysReq: {}".format(genreStrGOG[:-1], developerGOG,companyGOG, releaseDateGOG, reqstrGOG))

# Steam test Scrapping

testUrl = "https://www.skidrowreloaded.com/art-of-rally-kenya-codex/"
headers2 = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36 OPR/77.0.4054.275"
            }
reqGamepage = Request(testUrl, headers=headers2)
webGamepage = urlopen(reqGamepage).read()

page_soupGame = soup(webGamepage, "html.parser")
idTabsVerifier = page_soupGame.find("div", {"class" : "wordpress-post-tabs"})

divid0 = idTabsVerifier.div["id"].replace("_","-") + "-0"
divid3 = idTabsVerifier.div["id"].replace("_","-") + "-3"
containerTitleandLinks = page_soupGame.find("div", {"id" : divid0})

sizeGameArrays = containerTitleandLinks.findChildren()[9].text.partition('\n')

currentGameSize = "0 GB"
for item in containerTitleandLinks.select("p"):
    currentp = item
    if "Size:" in item.text:
        currentGameSize = item.text.partition('\n')[-1][:-12]

containerYTLink = page_soupGame.find("div", {"id" : divid3}).iframe["src"]
print(containerYTLink)

    








    





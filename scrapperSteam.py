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
testUrl = "https://store.steampowered.com/app/1076620/Svoboda_1945_Liberation/"
reqGamepage = Request(testUrl)
webGamepage = urlopen(reqGamepage).read()

page_soupGame = soup(webGamepage, "html.parser")
containerInfoGame = page_soupGame.find_all("div", {"class":"dev_row"})
sysRequired = page_soupGame.find("div", {"class" : "game_area_sys_req"}).div.ul.find_all("li")

developer = (page_soupGame.find("div", {"id":"developers_list"}).text).partition('\n')[2]
publisher = containerInfoGame[1].a.text
releaseDate = (page_soupGame.find("div", {"class":"date"})).text
genre = ((page_soupGame.find("div", {"id":"genresAndManufacturer"})).text).partition('\n')[2].partition('\n')[2].partition('\n')[0]
ratings = page_soupGame.find("span", {"class":"game_review_summary"}).text
sysRequiredStr = ""
for req in sysRequired:
    sysRequiredStr = sysRequiredStr + "|" + req.text

videoLink = page_soupGame.find("div", {"class": "highlight_player_item"})["data-webm-source"]
print(videoLink)


    





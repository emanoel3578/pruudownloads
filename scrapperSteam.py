from urllib import request
from urllib.request import Request,urlopen
from bs4 import BeautifulSoup as soup
from bs4.element import ContentMetaAttributeValue

# Inicio do request para a pagina do jogo 

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

print(ratings)
    





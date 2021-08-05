from urllib import request
from urllib.request import Request,urlopen
from bs4 import BeautifulSoup as soup
from bs4.element import ContentMetaAttributeValue

gameTitle = "Svoboda1945:Liberation"
urlQuery = "https://store.steampowered.com/search/?term=" + gameTitle

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36 OPR/77.0.4054.275"
}

req = Request(urlQuery, headers=headers)
webpage = urlopen(req).read()

page_soup = soup(webpage, "html.parser")

containers = page_soup.find("div", {"id":"search_resultsRows"})
urlGamePage = containers.a["href"]

# Inicio do request para a pagina do jogo 

testUrl = "https://store.steampowered.com/app/1076620/Svoboda_1945_Liberation/"
reqGamepage = Request(testUrl)
webGamepage = urlopen(reqGamepage).read()

page_soupGame = soup(webGamepage, "html.parser")
containerInfoGame = page_soupGame.find_all("div", {"class":"dev_row"})

# devpubgenre = containerInfoGame.find_all("a")
releaseDate = (page_soupGame.find("div", {"class":"date"})).text


print(containerInfoGame)



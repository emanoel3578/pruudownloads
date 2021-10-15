from email import header
from urllib import request
import urllib
from urllib.request import Request,urlopen
from bs4 import BeautifulSoup as soup
from bs4.builder import TreeBuilder
from bs4.element import ContentMetaAttributeValue
import json
import requests



# GAME 3RB Scarping

# Scrapping da pagina de procura, pegando o primeiro item da procura...
# srcString= "The ascent"
# treatedString = srcString.replace(" ", "+")
# my_url = "https://www.game3rb.com/?s=" + str(treatedString)

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'
}

# req = Request(my_url, headers=headers)
# webpage = urlopen(req).read()

# page_soup = soup(webpage, "html.parser")
# mainPosts = page_soup.find("div", {"class":"main-posts"})
# try:
#     gameLink = mainPosts.find("h3", {"class":"entry-title"}).a["href"]
#     onlineName = mainPosts.find("h3", {"class":"entry-title"}).a.text
#     if "OnLine" in onlineName:
#         # Já dentro da pagina do jogo, Pegando os links do redirecionador
#         reqCurrentGame = Request(gameLink, headers=headers)
#         webPageCurrentGame = urlopen(reqCurrentGame).read()

#         page_soupGame = soup(webPageCurrentGame, "html.parser")
#         sourceDownloadLink = page_soupGame.find_all("a", {"id":"download-link"})

#         fullGameLink = sourceDownloadLink[0]["href"]
#         SteamFix = page_soupGame.find("a", {"class":"online"})["href"]

#         # Scraping dos links para download dentro da pagina do Redirecionador

#         # Full Game links
#         reqFullGame = Request(fullGameLink, headers=headers)
#         webFullGame = urlopen(reqFullGame).read()

#         page_soupFullGame = soup(webFullGame, "html.parser")
#         fullgameDLink = page_soupFullGame.find_all("li")

#         # Links para o fullgame
#         linksForFullGame = []
#         for item in fullgameDLink:
#             linksForFullGame.append(item.a["href"])

#         print(linksForFullGame, end="\n")

#         # Steam fix links
#         reqSteamfix = Request(SteamFix, headers=headers)
#         webSteamfix = urlopen(reqSteamfix).read()

#         page_soupSteamFix = soup(webSteamfix, "html.parser")
#         SteamfixDLink = page_soupSteamFix.find_all("li")

#         # links para o steamfix
#         linksForSteamfix = []
#         for item in SteamfixDLink:
#             linksForSteamfix.append(item.a["href"])

#         print("Link for Steam fix ", linksForSteamfix, end="\n")
# except:
#     print("Not found")


# Microsoft Scraping

# try:
#     reqGOG = Request("https://www.microsoft.com/en-us/p/minecraft-dungeons/9n8nj74fztg9", headers=headers)
#     webGamepage = urlopen(reqGOG).read()

#     page_soupGame = soup(webGamepage, "html.parser")
#     containerImgHeader = page_soupGame.find("div", {"class":"c-video-player"})
#     containerGamemode = page_soupGame.find("div", {"class" : "module-capabilities"}).find_all("a")
#     normatTitle = page_soupGame.find("h1", {"id" : "DynamicHeading_productTitle"}).text
#     convertedJson = json.loads(containerImgHeader["data-player-data"])

#     developer = page_soupGame.find("div", {"class" : "buybox-metadata"}).text.strip()
#     publisher = page_soupGame.find("div", {"class" : "buybox-metadata"}).text.strip()

#     gamemode = "Singleplayer"
#     for item in containerGamemode:
#         if "Online" in item.text:
#             gamemode = "Online"

#     imgHeaderMicrosoft = convertedJson["metadata"]["posterframeUrl"].replace("//", "https://")
#     stringInfo = imgHeaderMicrosoft + "$$" + developer + "$$" + publisher + "$$" + gamemode

#     infoMicrosoft = []
#     infoMicrosoft.append(normatTitle)
#     infoMicrosoft.append(stringInfo)
    
#     print(infoMicrosoft)
# except urllib.error.HTTPError as error:
#     if "503" in error:
#         print("Error 503")
#     else:
#         print(error)

# Steam Scraping

reqGamepage = Request("https://store.steampowered.com/app/1088790/Rebel_Inc_Escalation/")
webGamepage = urlopen(reqGamepage).read()

page_soupGame = soup(webGamepage, "html.parser")
containerInfoGame = page_soupGame.find_all("div", {"class":"dev_row"})
containerHeaderimg = page_soupGame.find("div", {"id":"gameHeaderImageCtn"})
# sysRequired = page_soupGame.find("div", {"class" : "game_area_sys_req"}).div.ul.find_all("li")

imgHeader = containerHeaderimg.img["src"]
developer = (page_soupGame.find("div", {"id":"developers_list"}).text).partition('\n')[2]
publisher = containerInfoGame[1].a.text
try:
    videoLink = page_soupGame.find("div", {"class": "highlight_player_item"})["data-webm-source"]
except:
    videoLink="Empty"
containerGamemode = page_soupGame.find("div", {"id":"category_block"}).find_all("a")
gamemode = "Singleplayer"
for item in containerGamemode:
    if "Online" in item.text:
        gamemode = "Online"
try:
    ratings = page_soupGame.find("span", {"class":"game_review_summary"}).text
except AttributeError:
    ratings = (((page_soupGame.find("div", {"class":"summary"}).text).partition('\n')[2]).replace("\t", ""))

normalTitle = page_soupGame.find("div", {"id": "appHubAppName"}).text
Stringinfo = imgHeader + "$$" + developer + "$$" + publisher + "$$" + ratings + "$$" + videoLink + "$$" + gamemode

# myobj = {
#     'normaltitle':normalTitle,
#     'imgheader':imgHeader,
#     'developer':developer,
#     'publisher':publisher,
#     'ratings':ratings,
#     'videolink':videoLink,
#     'gamemode':gamemode,
# }

# url = "http://127.0.0.1:8000/api/newGame"
# req = requests.post(url, data = myobj)

# print(req.text)

infoSteam = []
infoSteam.append(normalTitle)
infoSteam.append(Stringinfo)
print(infoSteam)


# GOG Scraping
# reqGOG = Request("https://www.gog.com/game/crossroads_inn_collectors_edition_limited_bundle")
# webpageGOG = urlopen(reqGOG).read()

# page_soupGOG = soup(webpageGOG, "html.parser")
# genreGOG = page_soupGOG.find_all("div", {"class":"table--without-border"})
# print(genreGOG)
# if len(genreGOG) != 0:
#     developerGOG = genreGOG[-1].select("div:-soup-contains('Company')")[0].find_all_next("a")[0].text
#     companyGOG = genreGOG[-1].select("div:-soup-contains('Company')")[0].find_all_next("a")[1].text
#     imgHeaderGOG = page_soupGOG.find("img", {"class" : "mobile-slider__image"})["src"]
#     containerGamemode = page_soupGOG.find_all("a", {"class":"details__feature"})
#     normalTitle = page_soupGOG.find("h1", {"class":"productcard-basics__title"}).text
#     for item in containerGamemode:
#         if "Multi" in  item.text:
#             gamemode = "Online"
#         else:
#             gamemode = "Singleplayer"
#     ratingsGOG = "Nothing"

#     stringInfo = imgHeaderGOG + "$$" + developerGOG + "$$" + companyGOG + "$$" + ratingsGOG + "$$" + gamemode
#     infoGOG = []
#     infoGOG.append(normalTitle) 
#     infoGOG.append(stringInfo) 

#     print(infoGOG) 
# else:
#     print ("Empty")

# Epic Scraping

# reqGamepage = Request("https://www.epicgames.com/store/en-US/p/detroit-become-human")
# webGamepage = urlopen(reqGamepage).read()

# page_soupGame = soup(webGamepage, "html.parser")
# containerDev = page_soupGame.find_all("div", {"data-component":"PDPSidebarMetadataBase"})
# containerImg = page_soupGame.find_all("div", {"data-component":"PDPSidebarLogo"})
# containerGamemode = page_soupGame.find_all("div", {"data-component":"AboutMetadataLayout"})[-1]
# normalTitle = page_soupGame.find("div", {"data-component":"PDPTitleHeader"}).span.text
# GamemodeUL = containerGamemode.find("ul")
# if GamemodeUL == None:
#     gamemode = "Singleplayer"
# else:
#     for item in GamemodeUL:
#         if "Single Player" == item.text:
#             gamemode = "Singleplayer"
#         else:
#             gamemode = "Online"

# imgHeader = containerImg[1].div.img["src"]
# developer = containerDev[0].span.find_next().text
# publisher = containerDev[1].span.find_next().text

# infoEpic = imgHeader + "$$" + developer + "$$" + publisher + "$$" + gamemode
# print(normalTitle)

# Skidrow test Scrapping

# testUrl = "https://www.skidrowreloaded.com/star-wars-battlefront-ii-celebration-edition-empress/"
# headers2 = {
#                 "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36 OPR/77.0.4054.275"
#             }
# reqGamepage = Request(testUrl, headers=headers2)
# webGamepage = urlopen(reqGamepage).read()

# page_soupGame = soup(webGamepage, "html.parser")
# idTabsVerifier = page_soupGame.find("div", {"class" : "wordpress-post-tabs"})

# divid0 = idTabsVerifier.div["id"].replace("_","-") + "-0"
# divid3 = idTabsVerifier.div["id"].replace("_","-") + "-3"
# containerTitleandLinks = page_soupGame.find("div", {"id" : divid0})

# sizeGameArrays = containerTitleandLinks.findChildren()[9].text.partition('\n')

# currentGameSize = "0 GB"
# for item in containerTitleandLinks.select("p"):
#     currentp = item
#     if "Size:" in item.text:
#         currentGameSize = item.text.partition('\n')[-1][:-12]

# containerYTLink = page_soupGame.find("div", {"id" : divid3}).iframe["src"]

# containerSysReq = page_soupGame.find_all("div", {"class" : "game_area_sys_req_leftCol"})[-1].find_all("p")[1].text
# print(containerSysReq.replace('\n', "$$"))

# ProductLink = "https://store.steampowered.com/app/1070860/Serin_Fate/"


# def infoGamesSteam(ProductLink,triesSteam):
#     if triesSteam < 3:
#         try:
#             reqGamepage = Request(ProductLink)
#             webGamepage = urlopen(reqGamepage).read()

#             page_soupGame = soup(webGamepage, "html.parser")
#             containerInfoGame = page_soupGame.find_all("div", {"class":"dev_row"})
#             containerHeaderimg = page_soupGame.find("div", {"id":"gameHeaderImageCtn"})
#             # sysRequired = page_soupGame.find("div", {"class" : "game_area_sys_req"}).div.ul.find_all("li")

#             imgHeader = containerHeaderimg.img["src"]
#             developer = (page_soupGame.find("div", {"id":"developers_list"}).text).partition('\n')[2]
#             publisher = containerInfoGame[1].a.text
#             try:
#                 videoLink = page_soupGame.find("div", {"class": "highlight_player_item"})["data-webm-source"]
#             except:
#                 videoLink="Empty"
#             containerGamemode = page_soupGame.find("div", {"id":"category_block"}).find_all("a")
#             gamemode = "Singleplayer"
#             for item in containerGamemode:
#                 if "Online" in item.text:
#                     gamemode = "Online"
#             try:
#                 ratings = page_soupGame.find("span", {"class":"game_review_summary"}).text
#             except AttributeError:
#                 ratings = (((page_soupGame.find("div", {"class":"summary"}).text).partition('\n')[2]).replace("\t", ""))
#             # sysRequiredStr = ""
#             # for req in sysRequired:
#             #     treatedReq = req.text.replace("|", "")
#             #     sysRequiredStr = sysRequiredStr + "|" + treatedReq
#             # if "Roguebook" in ProductLink:
#             #     print(sysRequiredStr)

#             infoSteam = imgHeader + "$$" + developer + "$$" + publisher + "$$" + ratings + "$$" + videoLink + "$$" + gamemode
#             return infoSteam
#             # return print("{} // Developer: {} // Publisher: {} // Release Date: {} // Ratings: {} // SysReq: {}".format(genre, developer,publisher, releaseDate, ratings, sysRequiredStr))
#         except:
#             print("Something went wrong on steam link" + ProductLink)
#             return False
#     else:
#         print("Tried three times but something didn't work on Steam link")


# triesSteam = 0
# infoDeveloper = infoGamesSteam(ProductLink,triesSteam)
# while infoGamesSteam(ProductLink,triesSteam) == False:
#     triesSteam= triesSteam + 1
# if (infoDeveloper == False and triesSteam == 3):
#     infoDeveloper = "Empty"

# print(infoDeveloper)
    








    





from urllib import request
from urllib.request import Request,urlopen
from bs4 import BeautifulSoup as soup
from bs4.builder import TreeBuilder
from bs4.element import ContentMetaAttributeValue
import json


# Microsoft Scraping

# reqGOG = Request("https://www.microsoft.com/en-us/p/minecraft-dungeons/9n8nj74fztg9?activetab=pivot:overviewtab")
# webpage = urlopen(reqGOG).read()

# page_soupGame = soup(webpage, "html.parser")
# containerImgHeader = page_soupGame.find("div", {"class":"c-video-player"})
# containerGamemode = page_soupGame.find("div", {"class" : "module-capabilities"}).find_all("a")
# convertedJson = json.loads(containerImgHeader["data-player-data"])

# developer = page_soupGame.find("div", {"class" : "buybox-metadata"}).text.strip()
# publisher = page_soupGame.find("div", {"class" : "buybox-metadata"}).text.strip()

# gamemode = "Singleplayer"
# for item in containerGamemode:
#     if "Online" in item.text:
#         gamemode = "Online"
# imgHeaderMicrosoft = convertedJson["metadata"]["posterframeUrl"].replace("//", "https://")

# infoMicrosoft = imgHeaderMicrosoft + "$$" + developer + "$$" + publisher + "$$" + gamemode

# print(containerGamemode)

# Steam Scraping

# reqGOG = Request("https://store.steampowered.com/app/1257640/Dreamscaper_Prologue__Supporters_Edition/")
# webpage = urlopen(reqGOG).read()

# page_soupGame = soup(webpage, "html.parser")
# containerInfoGame = page_soupGame.find_all("div", {"class":"dev_row"})
# containerHeaderimg = page_soupGame.find("div", {"id":"gameHeaderImageCtn"})
# # sysRequired = page_soupGame.find("div", {"class" : "game_area_sys_req"}).div.ul.find_all("li")

# imgHeader = containerHeaderimg.img["src"]
# developer = (page_soupGame.find("div", {"id":"developers_list"}).text).partition('\n')[2]
# publisher = containerInfoGame[1].a.text
# try:
#     videoLink = page_soupGame.find("div", {"class": "highlight_player_item"})["data-webm-source"]
# except:
#     videoLink="Empty"
# containerGamemode = page_soupGame.find("div", {"id":"category_block"}).find_all("a")
# gamemode = "Singleplayer"
# for item in containerGamemode:
#     if "Online" in item.text:
#         gamemode = "Online"
# try:
#     ratings = page_soupGame.find("span", {"class":"game_review_summary"}).text
# except AttributeError:
#     ratings = (((page_soupGame.find("div", {"class":"summary"}).text).partition('\n')[2]).replace("\t", ""))
# sysRequiredStr = ""
# for req in sysRequired:
#     treatedReq = req.text.replace("|", "")
#     sysRequiredStr = sysRequiredStr + "|" + treatedReq
# if "Roguebook" in ProductLink:
#     print(sysRequiredStr)

# infoSteam = imgHeader + "$$" + developer + "$$" + publisher + "$$" + ratings + "$$" + videoLink + "$$" + gamemode


# GOG Scraping
reqGOG = Request("https://www.gog.com/game/out_of_line")
webpageGOG = urlopen(reqGOG).read()

page_soupGOG = soup(webpageGOG, "html.parser")
genreGOG = page_soupGOG.find_all("div", {"class":"table--without-border"})

if len(genreGOG) != 0:
    developerGOG = genreGOG[-1].select("div:-soup-contains('Company')")[0].find_all_next("a")[0].text
    companyGOG = genreGOG[-1].select("div:-soup-contains('Company')")[0].find_all_next("a")[1].text
    imgHeaderGOG = page_soupGOG.find("img", {"class" : "mobile-slider__image"})["src"]
    containerGamemode = page_soupGOG.find_all("a", {"class":"details__feature"})
for item in containerGamemode:
    if "Multi" in  item.text:
        gamemode = "Online"
    else:
        gamemode = "Singleplayer"
ratingsGOG = "Nothing"

# infoGOG = imgHeaderGOG + "$$" + developerGOG + "$$" + companyGOG + "$$" + ratingsGOG + "$$" + gamemode
print(developerGOG)

# Epic Scaping

# reqGamepage = Request("https://www.epicgames.com/store/en-US/p/red-dead-redemption-2")
# webGamepage = urlopen(reqGamepage).read()

# page_soupGame = soup(webGamepage, "html.parser")
# containerDev = page_soupGame.find_all("div", {"data-component":"PDPSidebarMetadataBase"})
# containerImg = page_soupGame.find_all("div", {"data-component":"PDPSidebarLogo"})
# containerGamemode = page_soupGame.find_all("div", {"data-component":"AboutMetadataLayout"})[-1].find("ul")
# for item in containerGamemode:
#     if "Single Player" == item.text:
#         gamemode = "Singleplayer"
#     else:
#         gamemode = "Online"

# print(gamemode)


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

# ProductLink = "https://store.steampowered.com/app/1693190/Evdeki_Lanet/"


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
    








    





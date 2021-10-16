from csv import reader
from os import error, name
from urllib import request
import urllib
from urllib.request import Request,urlopen
from bs4 import BeautifulSoup as soup
from bs4.element import ContentMetaAttributeValue
import json
import sys
import itertools
import requests
import traceback



#Funçaõ para pegar informções sobre o jogo
def infoGamesSteam(ProductLink,triesSteam):
    if triesSteam < 3:
        try:
            reqGamepage = Request(ProductLink)
            webGamepage = urlopen(reqGamepage).read()

            page_soupGame = soup(webGamepage, "html.parser")
            containerInfoGame = page_soupGame.find_all("div", {"class":"dev_row"})
            containerHeaderimg = page_soupGame.find("div", {"id":"gameHeaderImageCtn"})

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
            # Stringinfo = imgHeader + "$$" + developer + "$$" + publisher + "$$" + ratings + "$$" + videoLink + "$$" + gamemode

            myobj = {
                    'normaltitle':normalTitle,
                    'imgheader':imgHeader,
                    'developer':developer,
                    'publisher':publisher,
                    'ratings':ratings,
                    'videolink':videoLink,
                    'gamemode':gamemode,
                }

            infoSteam = myobj
            return infoSteam
            
        except Exception as e :
            print("Something went wrong on steam link " + ProductLink, end="")
            print(e)
            return False
    else:
        print("Tried three times but something didn't work on Steam link")
        crashedPageSteam = "Empty"
        return crashedPageSteam


def infoGamesEpic(ProductLink,triesEpic):
    if triesEpic < 3:
        try:
            reqGamepage = Request(ProductLink)
            webGamepage = urlopen(reqGamepage).read()

            page_soupGame = soup(webGamepage, "html.parser")
            containerDev = page_soupGame.find_all("div", {"data-component":"PDPSidebarMetadataBase"})
            containerImg = page_soupGame.find_all("div", {"data-component":"PDPSidebarLogo"})
            containerGamemode = page_soupGame.find_all("div", {"data-component":"AboutMetadataLayout"})[-1]
            normalTitle = page_soupGame.find("div", {"data-component":"PDPTitleHeader"}).span.text
            GamemodeUL = containerGamemode.find("ul")
            if GamemodeUL == None:
                gamemode = "Singleplayer"
            else:
                for item in GamemodeUL:
                    if "Single Player" == item.text:
                        gamemode = "Singleplayer"
                    else:
                        gamemode = "Online"

            imgHeader = containerImg[1].div.img["src"]
            developer = containerDev[0].span.find_next().text
            publisher = containerDev[1].span.find_next().text

            # stringInfo = imgHeader + "$$" + developer + "$$" + publisher + "$$" + gamemode

            myobj = {
                    'normaltitle':normalTitle,
                    'imgheader':imgHeader,
                    'developer':developer,
                    'publisher':publisher,
                    'gamemode':gamemode,
                }

            infoEpic = myobj
            return infoEpic

        except Exception as e:
            print("Something went wrong on Epic link" + " " + ProductLink)
            print(e)
            return False
    else:
        print("Tried three times but something didn't work on Epic link")
        crashedPageEpic = "Empty"
        return crashedPageEpic


def infoGamesMicrosoft(ProductLink,triesMicrosoft):
    if triesMicrosoft < 3:
        try:
            reqGamepage = Request(ProductLink)
            webGamepage = urlopen(reqGamepage).read()

            page_soupGame = soup(webGamepage, "html.parser")
            containerImgHeader = page_soupGame.find("div", {"class":"c-video-player"})
            containerGamemode = page_soupGame.find("div", {"class" : "module-capabilities"}).find_all("a")
            normatTitle = page_soupGame.find("h1", {"id" : "DynamicHeading_productTitle"}).text
            convertedJson = json.loads(containerImgHeader["data-player-data"])

            developer = page_soupGame.find("div", {"class" : "buybox-metadata"}).text.strip()
            publisher = page_soupGame.find("div", {"class" : "buybox-metadata"}).text.strip()

            gamemode = "Singleplayer"
            for item in containerGamemode:
                if "Online" in item.text:
                    gamemode = "Online"

            imgHeaderMicrosoft = convertedJson["metadata"]["posterframeUrl"].replace("//", "https://")
            # stringInfo = imgHeaderMicrosoft + "$$" + developer + "$$" + publisher + "$$" + gamemode

            myobj = {
                    'normaltitle':normatTitle,
                    'imgheader':imgHeaderMicrosoft,
                    'developer':developer,
                    'publisher':publisher,
                    'gamemode':gamemode,
                }

            infoMicrosoft = myobj
            
            return infoMicrosoft

        except Exception as e:
            print("Something went wrong on Microsoft link ", ProductLink)
            print(e)
            return False
    else:
        print("Tried three times but something didn't work on Microsoft link")
        crashedPageMicrosoft = "Empty"
        return crashedPageMicrosoft


def infoGamesGOG(ProductLink,triesGOG):
    if triesGOG < 3:
        try:
            reqGOG = Request(ProductLink)
            webpageGOG = urlopen(reqGOG).read()

            page_soupGOG = soup(webpageGOG, "html.parser")
            genreGOG = page_soupGOG.find_all("div", {"class":"table--without-border"})

            if len(genreGOG) != 0:
                developerGOG = genreGOG[-1].select("div:-soup-contains('Company')")[0].find_all_next("a")[0].text
                companyGOG = genreGOG[-1].select("div:-soup-contains('Company')")[0].find_all_next("a")[1].text
                imgHeaderGOG = page_soupGOG.find("img", {"class" : "mobile-slider__image"})["src"]
                containerGamemode = page_soupGOG.find_all("a", {"class":"details__feature"})
                try:
                    normalTitle = page_soupGOG.find("h1", {"class":"productcard-basics__title"}).text
                except:
                    normalTitle = "Not found"
                for item in containerGamemode:
                    if "Multi" in  item.text:
                        gamemode = "Online"
                    else:
                        gamemode = "Singleplayer"
                ratingsGOG = "Nothing"

                # stringInfo = imgHeaderGOG + "$$" + developerGOG + "$$" + companyGOG + "$$" + ratingsGOG + "$$" + gamemode

                myobj = {
                    'normaltitle':normalTitle,
                    'imgheader':imgHeaderGOG,
                    'developer':developerGOG,
                    'publisher':companyGOG,
                    'ratings':ratingsGOG,
                    'gamemode':gamemode,
                }
                
                infoGOG = myobj
                return infoGOG
            else:
                print ("Empty ", ProductLink)
                crashedPageGOG = "Empty"
                return crashedPageGOG

        except Exception as errorexec:
            print("Something went wrong on GOG link" + ProductLink)
            print(errorexec)
            return False
    else:
        print("Tried three times but something didn't work on GOG link")
        crashedPageGog = "Empty"
        return crashedPageGog


with open('dict.json', 'r') as fp:
    loadedDict = json.load(fp)


# runFullDB = True
# # len(loadedDict) != 0
# if runFullDB == False:
#     currentPageUrl = "https://www.skidrowreloaded.com"
#     headers1 = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36 OPR/77.0.4054.275"
#     }
#     req1 = Request(currentPageUrl, headers=headers1)
#     webpage1 = urlopen(req1).read()

#     page_soup1 = soup(webpage1, "html.parser")
#     containers1 = page_soup1.findAll("div", {"class":"post"})

#     reversedDict = {}
#     for item in reversed(loadedDict):
#         reversedDict[item] = loadedDict[item]

#     firstItemsLoadedDict = dict(itertools.islice(loadedDict.items(), 9))

#     for container in containers1:
#         releaseTitle = container.h2.a.text
#         reversedlinksDict = {}
#         if(releaseTitle not in firstItemsLoadedDict):
#             linkcontainer= container.h2.a["href"]
                
#             my_url = linkcontainer
#             headers2 = {
#                 "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36 OPR/77.0.4054.275"
#             }
#             req2 = Request(my_url, headers=headers2)
#             webpage2 = urlopen(req2).read()

#             page_soup2 = soup(webpage2, "html.parser")
#             idTabsVerifier = page_soup2.find("div", {"class" : "wordpress-post-tabs"})

#             divid0 = idTabsVerifier.div["id"].replace("_","-") + "-0"
#             divid2 = idTabsVerifier.div["id"].replace("_","-") + "-2"
#             divid3 = idTabsVerifier.div["id"].replace("_","-") + "-3"
            
#             containerTitleandLinks = page_soup2.find("div", {"id" : divid0})
#             containerScreenshots = (page_soup2.find("div", {"id" : divid2})).find_all("img")
#             containerSysReq = (page_soup2.find("ul", {"class" : "bb_ul"}))

#             sysReq = ""
#             if containerSysReq != None:
#                 containerSysReq = containerSysReq.find_all("li")
#                 for li in containerSysReq:
#                     treatedReq = li.text.replace("|", "")
#                 sysReq = sysReq + "$$" + treatedReq
#             else :
#                 try:
#                     containerSysReq = page_soup2.find_all("div", {"class" : "game_area_sys_req_leftCol"})[-1].find_all("p")[1].text.replace('\n', "$$")
#                     sysReq = containerSysReq
#                     print("Something off with Requirements" + my_url)
#                 except:
#                     containerSysReq = "No requirements"
            
#             screenshotsLinks = (containerScreenshots[1]["src"] + "$$" + containerScreenshots[3]["src"])

#             ProductLink = containerTitleandLinks.a["href"]
    
#             genreGame = (page_soup2.find("div", {"id" : divid0})).find("p").findNext().text.partition('\n')[-1].partition('\n')[0]

#             descriptionGame = containerTitleandLinks.p.text

#             releaseDateGame = (page_soup2.find("div", {"id" : divid0})).find("p").findNext().text.partition('\n')[-1].partition('\n')[-1]

#             sizeGameArrays = containerTitleandLinks.findChildren()[9].text.partition('\n')

#             textcontainer = container.h2.a.text
            
#             YTLink = page_soup2.find("div", {"id" : divid3}).iframe["src"]

#             #Product info scraping starts here
#             triesSteamUpdate = 0
#             triesGOGUpdate = 0
#             triesEpicUpdate = 0
#             triesMicrosoftUpdate = 0
#             if "gog.com" in ProductLink:
#                 infoDeveloper = infoGamesGOG(ProductLink,triesGOGUpdate)
#                 while infoGamesGOG(ProductLink,triesGOGUpdate) == False:
#                     triesGOGUpdate = triesGOGUpdate + 1
#                 # print(ProductLink)
#             elif "steampowered" in ProductLink:
#                 infoDeveloper = infoGamesSteam(ProductLink,triesSteamUpdate)
#                 while infoGamesSteam(ProductLink,triesSteamUpdate) == False:
#                     triesSteamUpdate= triesSteamUpdate + 1
#                 # if (infoDeveloper == False and triesSteamUpdate == 3):
#                 #     infoDeveloper = "Empty"
#                 # print(ProductLink)
#             elif "epicgames" in ProductLink:
#                 infoDeveloper = infoGamesEpic(ProductLink,triesEpicUpdate)
#                 while infoGamesEpic(ProductLink,triesEpicUpdate) == False:
#                     triesEpicUpdate= triesEpicUpdate + 1
#                 # print(ProductLink)
#             elif "microsoft" in ProductLink:
#                 infoDeveloper = infoGamesMicrosoft(ProductLink,triesMicrosoftUpdate)
#                 while infoGamesMicrosoft(ProductLink,triesMicrosoftUpdate) == False:
#                     triesMicrosoftUpdate= triesMicrosoftUpdate + 1
#                 # print(ProductLink)
#             else:
#                 print(ProductLink)
#                 print("Not ready yet")
#                 infoDeveloper = "Empty"
                

#             listLinks = []
#             for a in containerTitleandLinks.find_all("a", href=True):
#                 if "skidrow" not in a["href"]:
#                     listLinks.append(a["href"])

#             #Getting the size of games
#             currentGameSize = "0 GB"
#             for item in containerTitleandLinks.select("p"):
#                 if "Size:" in item.text:
#                     currentGameSize = item.text.partition('\n')[-1][:-12]

#             #Getting the providers link
#             providerLinks = ""


#             for item in listLinks[2:]:
#                 if "zippyshare" in item:
#                     providerLinks = providerLinks + "$$" + item
#                 elif "mediafire" in item:
#                     providerLinks = providerLinks + "$$" + item
#                 elif "bowfile" in item:
#                     providerLinks = providerLinks + "$$" + item
#                 elif "mega.nz" in item:
#                     providerLinks = providerLinks + "$$" + item
#                 elif "magnet" in item:
#                     providerLinks = providerLinks + "$$" + item
                    
                
#             if infoDeveloper != "Empty":
#                 reversedlinksDict = providerLinks[2:] + "|" + sysReq[2:] + "|" + genreGame + "|" + releaseDateGame + "|" + descriptionGame + "|" + screenshotsLinks + "|" + ProductLink + "|" + infoDeveloper + "|" + YTLink + "|" + currentGameSize

#             reversedDict[releaseTitle] = reversedlinksDict

#     normalDict = {}
#     for item in reversed(reversedDict):
#         normalDict[item] = reversedDict[item]
    
#     with open('dict.json', 'w') as fp:
#             json.dump(normalDict, fp)
    

i = 200
linksDict = {}
while i > 0:
    try:
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
            
            my_url = linkcontainer
            headers2 = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36 OPR/77.0.4054.275"
            }
            req2 = Request(my_url, headers=headers2)
            webpage2 = urlopen(req2).read()

            page_soup2 = soup(webpage2, "html.parser")
            idTabsVerifier = page_soup2.find("div", {"class" : "wordpress-post-tabs"})

            divid0 = idTabsVerifier.div["id"].replace("_","-") + "-0"
            divid2 = idTabsVerifier.div["id"].replace("_","-") + "-2"
            divid3 = idTabsVerifier.div["id"].replace("_","-") + "-3"
            
            containerTitleandLinks = page_soup2.find("div", {"id" : divid0})
            containerScreenshots = (page_soup2.find("div", {"id" : divid2})).find_all("img")
            containerNameref = page_soup2.find('div', {'id': 'overall-container'})
            containerSysReq = (page_soup2.find("ul", {"class" : "bb_ul"}))

            sysReq = ""
            if containerSysReq != None:
                containerSysReq = containerSysReq.find_all("li")
                for li in containerSysReq:
                    treatedReq = li.text.replace("|", "")
                    sysReq = sysReq + "$$" + treatedReq
            else :
                try:
                    containerSysReq = page_soup2.find_all("div", {"class" : "game_area_sys_req_leftCol"})[-1].find_all("p")[1].text.replace('\n', "$$")
                    sysReq = containerSysReq
                    print("Something off with Requirements" + my_url)
                except:
                    containerSysReq = "No requirements"
            
            screenshotsLinks = (containerScreenshots[1]["src"] + "$$" + containerScreenshots[3]["src"])

            ProductLink = containerTitleandLinks.a["href"]

            nameref = containerNameref.div.h2.text

            genreGame = (page_soup2.find("div", {"id" : divid0})).find("p").findNext().text.partition('\n')[-1].partition('\n')[0]

            descriptionGame = containerTitleandLinks.p.text

            releaseDateGame = (page_soup2.find("div", {"id" : divid0})).find("p").findNext().text.partition('\n')[-1].partition('\n')[-1]

            sizeGameArrays = containerTitleandLinks.findChildren()[9].text.partition('\n')

            textcontainer = container.h2.a.text
            
            YTLink = page_soup2.find("div", {"id" : divid3}).iframe["src"]

            #Product info scraping starts here
            triesSteam = 0
            triesGOG = 0
            triesEpic = 0
            triesMicrosoft = 0
            if "gog.com" in ProductLink:
                infoDeveloper = infoGamesGOG(ProductLink,triesGOG)
                while infoGamesGOG(ProductLink,triesGOG) == False:
                    triesGOG = triesGOG + 1
                # print(ProductLink)
            elif "steampowered" in ProductLink:
                infoDeveloper = infoGamesSteam(ProductLink,triesSteam)
                while infoGamesSteam(ProductLink,triesSteam) == False:
                    triesSteam= triesSteam + 1
                    
                if (infoDeveloper == False and triesSteam == 3):
                    infoDeveloper = "Empty"
                # print(ProductLink)
            elif "epicgames" in ProductLink:
                infoDeveloper = infoGamesEpic(ProductLink,triesEpic)
                while infoGamesEpic(ProductLink,triesEpic) == False:
                    triesEpic= triesEpic + 1
                # print(ProductLink)
            elif "microsoft" in ProductLink:
                infoDeveloper = infoGamesMicrosoft(ProductLink,triesMicrosoft)
                while infoGamesMicrosoft(ProductLink,triesMicrosoft) == False:
                    triesMicrosoft= triesMicrosoft + 1
                # print(ProductLink)
            else:
                print(ProductLink)
                print("Not ready yet")
                infoDeveloper = "Empty"
                
            linksForFullGame = ""
            linksForSteamfix = ""

            if infoDeveloper != "Empty":
                if infoDeveloper['gamemode'] == "Online":
                    nameOfGameSearch = infoDeveloper['normaltitle'].split(" ")
                    if len(nameOfGameSearch) >= 3:
                        for a in range(2):
                            if a == 0:
                                srcString = nameOfGameSearch[a] + " " + nameOfGameSearch[a + 1]
                            else:
                                srcString = nameOfGameSearch[0] + " " + nameOfGameSearch[a] + " " + nameOfGameSearch[a + 1]

                            treatedString = srcString.replace(" ", "+").replace("™", "").replace("®", "").replace("ö", "")
                            my_url = "https://www.game3rb.com/?s=" + treatedString
                            # print(my_url)

                            headers = {
                                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'
                            }

                            req = Request(my_url, headers=headers)
                            webpage = urlopen(req).read()
                            
                            page_soup = soup(webpage, "html.parser")
                            mainPosts = page_soup.find("div", {"class":"main-posts"})
                            try:
                                gameLink = mainPosts.find("h3", {"class":"entry-title"}).a["href"]
                                onlineName = mainPosts.find("h3", {"class":"entry-title"}).a.text
                                if "OnLine" in onlineName:
                                    # Já dentro da pagina do jogo, Pegando os links do redirecionador
                                    reqCurrentGame = Request(gameLink, headers=headers)
                                    webPageCurrentGame = urlopen(reqCurrentGame).read()

                                    page_soupGame = soup(webPageCurrentGame, "html.parser")
                                    sourceDownloadLink = page_soupGame.find_all("a", {"id":"download-link"})

                                    fullGameLink = sourceDownloadLink[0]["href"]
                                    SteamFix = page_soupGame.find("a", {"class":"online"})["href"]

                                    # Scraping dos links para download dentro da pagina do Redirecionador

                                    # Full Game links
                                    reqFullGame = Request(fullGameLink, headers=headers)
                                    webFullGame = urlopen(reqFullGame).read()

                                    page_soupFullGame = soup(webFullGame, "html.parser")
                                    fullgameDLink = page_soupFullGame.find_all("li")

                                    # Links para o fullgame
                                    linksForFullGame = []
                                    for item in fullgameDLink:
                                        linksForFullGame.append(item.a["href"])

                                    # print("Link for full game ", infoDeveloper[0], " ", linksForFullGame, end="\n")

                                    # Steam fix links
                                    reqSteamfix = Request(SteamFix, headers=headers)
                                    webSteamfix = urlopen(reqSteamfix).read()

                                    page_soupSteamFix = soup(webSteamfix, "html.parser")
                                    SteamfixDLink = page_soupSteamFix.find_all("li")

                                    # links para o steamfix
                                    linksForSteamfix = []
                                    for item in SteamfixDLink:
                                        linksForSteamfix.append(item.a["href"])
                                    

                                    # print("Link for Steam fix ", infoDeveloper[0], "", linksForSteamfix, end="\n")

                                    if len(linksForSteamfix) > 0 and len(linksForFullGame) > 0:
                                        break
                            except Exception as e:
                                print(e)
                                print("Not found for " + infoDeveloper['normaltitle'])
                    else:
                        srcString= infoDeveloper['normaltitle']
                        treatedString = srcString.replace(" ", "+").replace("™", "").replace("®", "")
                        my_url = "https://www.game3rb.com/?s=" + treatedString
                        # print("Short URL ", my_url)

                        headers = {
                            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'
                        }

                        req = Request(my_url, headers=headers)
                        webpage = urlopen(req).read()
                        
                        page_soup = soup(webpage, "html.parser")
                        mainPosts = page_soup.find("div", {"class":"main-posts"})
                        try:
                            gameLink = mainPosts.find("h3", {"class":"entry-title"}).a["href"]
                            onlineName = mainPosts.find("h3", {"class":"entry-title"}).a.text
                            if "OnLine" in onlineName:
                                # Já dentro da pagina do jogo, Pegando os links do redirecionador
                                reqCurrentGame = Request(gameLink, headers=headers)
                                webPageCurrentGame = urlopen(reqCurrentGame).read()

                                page_soupGame = soup(webPageCurrentGame, "html.parser")
                                sourceDownloadLink = page_soupGame.find_all("a", {"id":"download-link"})

                                fullGameLink = sourceDownloadLink[0]["href"]
                                SteamFix = page_soupGame.find("a", {"class":"online"})["href"]

                                # Scraping dos links para download dentro da pagina do Redirecionador

                                # Full Game links
                                reqFullGame = Request(fullGameLink, headers=headers)
                                webFullGame = urlopen(reqFullGame).read()

                                page_soupFullGame = soup(webFullGame, "html.parser")
                                fullgameDLink = page_soupFullGame.find_all("li")

                                # Links para o fullgame
                                linksForFullGame = []
                                for item in fullgameDLink:
                                    linksForFullGame.append(item.a["href"])

                                # print("Link for full game ", infoDeveloper[0], " ", linksForFullGame, end="\n")

                                # Steam fix links
                                reqSteamfix = Request(SteamFix, headers=headers)
                                webSteamfix = urlopen(reqSteamfix).read()

                                page_soupSteamFix = soup(webSteamfix, "html.parser")
                                SteamfixDLink = page_soupSteamFix.find_all("li")

                                # links para o steamfix
                                linksForSteamfix = []
                                for item in SteamfixDLink:
                                    linksForSteamfix.append(item.a["href"])

                                # print("Link for Steam fix ", infoDeveloper[0], "", linksForSteamfix, end="\n")
                        except:
                            print("Not found for " + infoDeveloper['normaltitle'])

            listLinks = []
            for a in containerTitleandLinks.find_all("a", href=True):
                if "skidrow" not in a["href"]:
                    listLinks.append(a["href"])

            #Getting the size of games
            currentGameSize = "0 GB"
            for item in containerTitleandLinks.select("p"):
                if "Size:" in item.text:
                    currentGameSize = item.text.partition('\n')[-1][:-12]

            #Getting the providers link
            providerLinks = ""

            if len(linksForFullGame) > 0 and len(linksForSteamfix) > 0:
                for item in linksForFullGame:
                    if "zippyshare" in item:
                        infoDeveloper['zippyshare'] = item
                    elif "mediafire" in item:
                        infoDeveloper['mediafire'] = item
                    elif "bowfile" in item:
                        infoDeveloper['bowfile'] = item
                    elif "mega.nz" in item:
                        infoDeveloper['mega'] = item
                    elif "magnet" in item:
                        infoDeveloper['magnet'] = item
                    else:
                        infoDeveloper['others'] = item
                
                for item in linksForSteamfix:
                    if "zippyshare" in item:
                        infoDeveloper['zippyshareSteamfix'] = item
                    elif "mediafire" in item:
                        infoDeveloper['mediafireSteamfix'] = item
                    elif "bowfile" in item:
                        infoDeveloper['bowfileSteamfix'] = item
                    elif "mega.nz" in item:
                        infoDeveloper['megaSteamfix'] = item
                    elif "magnet" in item:
                        infoDeveloper['magnetSteamfix'] = item
                    else:
                        infoDeveloper['othersSteamfix'] = item

                # print("Here is the links for the online games ", providerLinks[2:], end='\n\n')
                if infoDeveloper != "Empty":
                    # linksDict[textcontainer] = providerLinks[2:] + "|" + sysReq[2:] + "|" + genreGame + "|" + releaseDateGame + "|" + descriptionGame + "|" + screenshotsLinks + "|" + ProductLink + "|" + infoDeveloper[1] + "|" + YTLink + "|" + currentGameSize
                    infoDeveloper['nameref'] = nameref
                    infoDeveloper['img1'] = containerScreenshots[1]["src"]
                    infoDeveloper['img2'] = containerScreenshots[3]["src"]
                    infoDeveloper['pagelink'] = ProductLink
                    infoDeveloper['genre'] = genreGame
                    infoDeveloper['description'] = descriptionGame
                    infoDeveloper['releasedate'] = releaseDateGame
                    infoDeveloper['size'] = currentGameSize
                    infoDeveloper['ytlink'] = YTLink
                    infoDeveloper['sys_requirements'] = sysReq[2:]
                    infoDeveloper['page'] = str(i)

                    api = "http://127.0.0.1:8000/api/newGame"
                    req = requests.post(api, data = infoDeveloper)

                    print(req.text)

            else:
                if infoDeveloper != "Empty":
                    for item in listLinks[2:]:
                        if "zippyshare" in item:
                            infoDeveloper['zippyshare'] = item
                        elif "mediafire" in item:
                            infoDeveloper['mediafire'] = item
                        elif "bowfile" in item:
                            infoDeveloper['bowfile'] = item
                        elif "mega.nz" in item:
                            infoDeveloper['mega'] = item
                        elif "magnet" in item:
                            infoDeveloper['magnet'] = item

                
                    # linksDict[textcontainer] = providerLinks[2:] + "|" + sysReq[2:] + "|" + genreGame + "|" + releaseDateGame + "|" + descriptionGame + "|" + screenshotsLinks + "|" + ProductLink + "|" + infoDeveloper[1] + "|" + YTLink + "|" + currentGameSize
                    infoDeveloper['nameref'] = nameref
                    infoDeveloper['img1'] = containerScreenshots[1]["src"]
                    infoDeveloper['img2'] = containerScreenshots[3]["src"]
                    infoDeveloper['pagelink'] = ProductLink
                    infoDeveloper['genre'] = genreGame
                    infoDeveloper['description'] = descriptionGame
                    infoDeveloper['releasedate'] = releaseDateGame
                    infoDeveloper['size'] = currentGameSize
                    infoDeveloper['ytlink'] = YTLink
                    infoDeveloper['sys_requirements'] = sysReq[2:]
                    infoDeveloper['page'] = str(i)

                    api = "http://127.0.0.1:8000/api/newGame"
                    req = requests.post(api, data = infoDeveloper)

                    print(req.text)


            # print(linksDict, end='\n\n')
        i = i - 1
        print("Page:" + str(i))
    except Exception as e:
        # print("A error has ocurred:", end=" ")
        print("A error has ocurred: ", end='')
        print(traceback.format_exc())

# sys.stdout = open("declare.js", "w")
# jsonObjc = json.dumps(linksDict)
# print("export var jsonstr = {}".format(jsonObjc))

with open('dict.json', 'w') as fp:
    json.dump(linksDict, fp)
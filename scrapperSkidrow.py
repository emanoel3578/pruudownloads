from csv import reader
from urllib import request
import urllib
from urllib.request import Request,urlopen
from bs4 import BeautifulSoup as soup
from bs4.element import ContentMetaAttributeValue
import json
import sys

#Funçaõ para pegar informções sobre o jogo
def infoGamesSteam(ProductLink,triesSteam):
    if triesSteam < 3:
        try:
            reqGamepage = Request(ProductLink)
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
            # sysRequiredStr = ""
            # for req in sysRequired:
            #     treatedReq = req.text.replace("|", "")
            #     sysRequiredStr = sysRequiredStr + "|" + treatedReq
            # if "Roguebook" in ProductLink:
            #     print(sysRequiredStr)

            infoSteam = imgHeader + "$$" + developer + "$$" + publisher + "$$" + ratings + "$$" + videoLink + "$$" + gamemode
            return infoSteam
            # return print("{} // Developer: {} // Publisher: {} // Release Date: {} // Ratings: {} // SysReq: {}".format(genre, developer,publisher, releaseDate, ratings, sysRequiredStr))
        except:
            print("Something went wrong on steam link" + ProductLink)
            return False
    else:
        print("Tried three times but something didn't work on Steam link")


def infoGamesEpic(ProductLink,triesEpic):
    if triesEpic < 3:
        try:
            reqGamepage = Request(ProductLink)
            webGamepage = urlopen(reqGamepage).read()

            page_soupGame = soup(webGamepage, "html.parser")
            containerDev = page_soupGame.select("div[class*='PDPSidebarMetadata__value']")
            containerImg = page_soupGame.select("div[class*='Image__pictureWrapper']")
            containerGamemode = page_soupGame.select("a[class*='LinkableTag__link']")
            for item in containerGamemode:
                if "Multi" or "Co-op" in item.text:
                    gamemode = "Online"
                else:
                    gamemode = "Singleplayer"

            imgHeader = containerImg[1].div.img["src"]
            developer = containerDev[0].span.text
            publisher = containerDev[1].span.text

            infoEpic = imgHeader + "$$" + developer + "$$" + publisher + "$$" + gamemode
            return infoEpic

        except:
            print("Something went wrong on Epic link" + ProductLink)
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
            convertedJson = json.loads(containerImgHeader["data-player-data"])

            developer = page_soupGame.find("div", {"class" : "buybox-metadata"}).text.strip()
            publisher = page_soupGame.find("div", {"class" : "buybox-metadata"}).text.strip()

            gamemode = "Singleplayer"
            for item in containerGamemode:
                if "Online" in item.text:
                    gamemode = "Online"

            imgHeaderMicrosoft = convertedJson["metadata"]["posterframeUrl"].replace("//", "https://")

            infoMicrosoft = imgHeaderMicrosoft + "$$" + developer + "$$" + publisher + "$$" + gamemode
            return infoMicrosoft

        except:
            print("Something went wrong on Microsoft link" + ProductLink)
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
                developerGOG = genreGOG[-1].find_all("div", {"class" : "details__rating"})[2].div.findNext().find_all("a")[0].text
                companyGOG = genreGOG[-1].find_all("div", {"class" : "details__rating"})[2].div.findNext().find_all("a")[1].text
                imgHeaderGOG = page_soupGOG.find("img", {"class" : "mobile-slider__image"})["src"]
                containerGamemode = page_soupGOG.find_all("a", {"class":"details__feature"})
                for item in containerGamemode:
                    if "Multi" in  item.text:
                        gamemode = "Online"
                    else:
                        gamemode = "Singleplayer"
                ratingsGOG = "Nothing"

                infoGOG = imgHeaderGOG + "$$" + developerGOG + "$$" + companyGOG + "$$" + ratingsGOG + "$$" + gamemode
                return infoGOG
            else:
                return "Empty"

        except Exception as errorexec:
            print("Something went wrong on GOG link" + ProductLink)
            print(errorexec)
            return False
    else:
        print("Tried three times but something didn't work on GOG link")
        crashedPageGog = "Empty"
        return crashedPageGog
        

i = 1
linksDict = {}
while i < 200:
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
            containerSysReq = (page_soup2.find("ul", {"class" : "bb_ul"}))

            sysReq = ""
            if containerSysReq != None:
                containerSysReq = containerSysReq.find_all("li")
                for li in containerSysReq:
                    treatedReq = li.text.replace("|", "")
                sysReq = sysReq + "$$" + treatedReq
            else :
                containerSysReq = page_soup2.find_all("div", {"class" : "game_area_sys_req_leftCol"})[-1].find_all("p")[1].text.replace('\n', "$$")
                sysReq = containerSysReq
                print(my_url)

            
            screenshotsLinks = (containerScreenshots[1]["src"] + "$$" + containerScreenshots[3]["src"])

            ProductLink = containerTitleandLinks.a["href"]
    
            genreGame = (page_soup2.find("div", {"id" : divid0})).find("p").findNext().text.partition('\n')[-1].partition('\n')[0]

            descriptionGame = containerTitleandLinks.p.text

            releaseDateGame = (page_soup2.find("div", {"id" : divid0})).find("p").findNext().text.partition('\n')[-1].partition('\n')[-1]

            sizeGameArrays = containerTitleandLinks.findChildren()[9].text.partition('\n')

            textcontainer = (containerTitleandLinks.findChildren()[2].text).partition('\n')[0][7:]
            
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

            for item in listLinks[2:]:
                # print(item)
                if "zippyshare" in item:
                    providerLinks = providerLinks + "$$" + item
                elif "mediafire" in item:
                    providerLinks = providerLinks + "$$" + item
                elif "bowfile" in item:
                    providerLinks = providerLinks + "$$" + item
                elif "mega.nz" in item:
                    providerLinks = providerLinks + "$$" + item
                elif "magnet" in item:
                    providerLinks = providerLinks + "$$" + item

                linksDict[textcontainer] = providerLinks[2:] + "|" + sysReq[2:] + "|" + genreGame + "|" + releaseDateGame + "|" + descriptionGame + "|" + screenshotsLinks + "|" + ProductLink + "|" + infoDeveloper + "|" + YTLink + "|" + currentGameSize

            # print(linksDict, end='\n\n')
        i = i + 1
        print("Page:" + str(i))
    except urllib.error.URLError as e:
        print("A error has ocurred:", end=" ")
        print(e)


sys.stdout = open("declare.js", "w")
jsonObjc = json.dumps(linksDict)
print("export var jsonstr = {}".format(jsonObjc))
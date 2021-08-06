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
            sysRequired = page_soupGame.find("div", {"class" : "game_area_sys_req"}).div.ul.find_all("li")

            developer = (page_soupGame.find("div", {"id":"developers_list"}).text).partition('\n')[2]
            publisher = containerInfoGame[1].a.text
            releaseDate = (page_soupGame.find("div", {"class":"date"})).text
            genre = ((page_soupGame.find("div", {"id":"genresAndManufacturer"})).text).partition('\n')[2].partition('\n')[2].partition('\n')[0]
            try:
                ratings = page_soupGame.find("span", {"class":"game_review_summary"}).text
            except AttributeError:
                ratings = (((page_soupGame.find("div", {"class":"summary"}).text).partition('\n')[2]).replace("\t", ""))
            sysRequiredStr = ""
            for req in sysRequired:
                sysRequiredStr = sysRequiredStr + "|" + req.text

            # return print("{} // Developer: {} // Publisher: {} // Release Date: {} // Ratings: {} // SysReq: {}".format(genre, developer,publisher, releaseDate, ratings, sysRequiredStr))
            # return print("{} // Developer: {} // Publisher: {} // Release Date: {} // Ratings: {} // SysReq: {}".format(genre, developer,publisher, releaseDate, ratings, sysRequiredStr))
        except:
            print("Something went wrong on steam link")
            return False
    else:
        return print("Tried three times but something didn't work on Steam link")


def infoGamesGOG(ProductLink,triesGOG):
    if triesGOG < 3:
        try:
            reqGOG = Request(ProductLink)
            webpageGOG = urlopen(reqGOG).read()

            page_soupGOG = soup(webpageGOG, "html.parser")
            genreGOG = page_soupGOG.find_all("div", {"class":"table--without-border"})

            genreStrGOG = "|Genre:"
            releaseDateGOG = "00/00/00"
            developerGOG = genreGOG[-1].find_all("div", {"class" : "details__rating"})[2].div.findNext().find_all("a")[0].text
            companyGOG = genreGOG[-1].find_all("div", {"class" : "details__rating"})[2].div.findNext().find_all("a")[1].text
            apirul = "https://api.gog.com/v2/games/1455317728?locale=en-US"

            apiRequest = request.urlopen(apirul).read()
            apiContent = json.loads(apiRequest)
            reqstrGOG = ""

            for el in apiContent["_embedded"]["supportedOperatingSystems"][0]["systemRequirements"][0]["requirements"]:
                reqstrGOG = reqstrGOG + (el["name"] + el["description"]) + " "

            for genre in genreGOG[-1].div.find_all("a"):
                genreStrGOG = genreStrGOG + genre.text + "-"

            # return print("{} // Developer: {} // Publisher: {} // Release Date: {} // SysReq: {}".format(genreStrGOG[ :-1], developerGOG,companyGOG, releaseDateGOG, reqstrGOG))
            # return print("{} // Developer: {} // Publisher: {} // Release Date: {} // SysReq: {}".format(genreStrGOG[ :-1], developerGOG,companyGOG, releaseDateGOG, reqstrGOG))
        except:
            print("Something went wrong on GOG link")
            return False
    else:
        return print("Tried three times but something didn't work on GOG link")


i = 1
linksDict = {}
while i < 10:
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
            
            containerTitleandLinks = page_soup2.find("div", {"id" : divid0})
            containerScreenshots = (page_soup2.find("div", {"id" : divid2})).find_all("img")
            containerSysReq = (page_soup2.find("ul", {"class" : "bb_ul"})).find_all("li")

            sysReq = ""
            for li in containerSysReq:
                sysReq = sysReq + "|" + li.text
                
            screenshotsLinks = (containerScreenshots[1]["src"] + "|" + containerScreenshots[3]["src"])

            ProductLink = containerTitleandLinks.a["href"]
            
            genreGame = (page_soup2.find("div", {"id" : divid0})).find("p").findNext().text.partition('\n')[-1].partition('\n')[0]

            descriptionGame = containerTitleandLinks.p.text

            releaseDateGame = (page_soup2.find("div", {"id" : divid0})).find("p").findNext().text.partition('\n')[-1].partition('\n')[-1]

            sizeGameArrays = containerTitleandLinks.findChildren()[9].text.partition('\n')
            
            textcontainer = (containerTitleandLinks.findChildren()[2].text).partition('\n')[0][7:]

            # #Product info scraping starts here
            # triesGOG = 0
            # triesSteam = 0
            # if "gog.com" in ProductLink:
            #     while infoGamesGOG(ProductLink,triesGOG) == False:
            #         triesGOG = triesGOG + 1
            # elif "steam" in ProductLink:
            #     while infoGamesSteam(ProductLink,triesSteam) == False:
            #         triesSteam= triesSteam + 1
            # else:
            #     print("Not ready yet")

            listLinks = []
            for a in containerTitleandLinks.find_all("a", href=True):
                if "skidrow" not in a["href"]:
                    listLinks.append(a["href"])

            #Getting the size of games
            if "Size" not in sizeGameArrays[2].partition('\n')[0]:
                currentGameSize = "|0 GB"
            else:
                currentGameSize = "|" + sizeGameArrays[2].partition('\n')[0][6:]

            #Getting the providers link
            providerLinks = ""

            for item in listLinks[2:]:
                # print(item)
                if "zippyshare" in item:
                    providerLinks = providerLinks + "|" + item
                elif "mediafire" in item:
                    providerLinks = providerLinks + "|" + item
                elif "bowfile" in item:
                    providerLinks = providerLinks + "|" + item
                elif "mega.nz" in item:
                    providerLinks = providerLinks + "|" + item
                elif "magnet" in item:
                    providerLinks = providerLinks + "|" + item

                linksDict[textcontainer] = providerLinks[1:]  + "|" + ProductLink + currentGameSize

            # print(linksDict)
        i = i + 1
        print("Page:" + str(i))
    except urllib.error.URLError as e:
        print("A error has ocurred:", end=" ")
        print(e)


sys.stdout = open("declare.js", "w")
jsonObjc = json.dumps(linksDict)
print("export var jsonstr = {}".format(jsonObjc))
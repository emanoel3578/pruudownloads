<template>
    <div class="font-kanit">
        <div class="">
            <div class="flex justify-around bg-gray-400" id="top">
                <div class="flex">
                    <div>
                        <img id="pruulogo" src="/img/huelogov1.png" class="max-h-28 transform -translate-y-2 rotate-45">
                    </div>
                    <div class="flex items-center">
                        <span class="font-kanit text-xl text-white ml-2">PruuDownloads</span>
                    </div>
                </div>

                <div class="flex">
                    <div class="flex items-center">
                        <div class="flex items-center gap-2 rounded-full py-3 px-6 p-2 md:text-xl font-kanit text-white border-3 border-gray-100 bg-gradient-to-r hover:from-blue-500 hover:to-purple-400 hover:text-white cursor-pointer shadow-lg">
                            <label @click="searchbar = !searchbar" for="search" class="cursor-pointer ">Search for games</label>
                            <input v-model="searchQuery" v-show="searchbar" class="text-black" size="25">
                            <img @click="sendSearch" v-show="searchbar" src="/img/lupe.png">
                        </div>
                    </div>
                </div>
            </div>

            <div class="bg-gray-700 flex justify-center font-kanit">
                <ul class="flex list-none gap-5">
                    <li class="bg-white rounded-full border-2 border-black cursor-pointer hover:bg-purple-500 p-2 m-2">
                        <router-link :to="'/home'">
                            <a>Home</a>
                        </router-link>
                    </li>
                    <li class="bg-white rounded-full border-2 border-black cursor-pointer hover:bg-purple-500 p-2 m-2">
                        <router-link :to="'/pc-repack'">
                            <a>PC Repack</a>
                        </router-link>
                    </li>
                    <li class="bg-white rounded-full border-2 border-black cursor-pointer hover:bg-purple-500 p-2 m-2">
                        <router-link :to="'/gamesonline'">
                            <a>Games online</a>
                        </router-link>
                    </li>
                    <li class="bg-white rounded-full border-2 border-black cursor-pointer hover:bg-purple-500 p-2 m-2">
                        <router-link :to="'/howtodownload'">
                            <a>How to Download</a>
                        </router-link>
                    </li>
                    <li class="bg-white rounded-full border-2 border-black cursor-pointer hover:bg-purple-500 p-2 m-2">
                        <router-link :to="'/dmca'">
                            <a>DMCA</a>
                        </router-link>
                    </li>
                    <li class="bg-white rounded-full border-2 border-black cursor-pointer hover:bg-purple-500 p-2 m-2">
                        <router-link :to="'/aboutus'">
                            <a>About Us</a>
                        </router-link>
                    </li>
                </ul>
            </div>
        </div>

        <div class="mt-10 w-4/5 mx-auto my-0">
            <div class="flex">
                <div class="flex flex-col w-full">
                    <div class="flex text-white mb-5">
                        <div class="border-2 border-black bg-gray-800 px-3">
                            <a>{{(this.genre).replace(new RegExp(",", "g"), "/")}}</a>
                        </div>
                    </div>

                    <div class="flex flex-col text-white">
                        <div class="flex">
                            <p class="text-3xl">Download&nbsp;</p>
                            <p class="text-3xl">{{this.name}}</p>
                        </div>
                        <div class="flex mt-5">
                            <p>about&nbsp;</p>
                            <p>:time:</p>
                        </div>
                    </div>

                    <div class="flex justify-center">
                        <img :src="this.devInfo[0]" class="w-3/5 max-h-auto">
                    </div>

                    <div class="flex flex-col ">
                        <div class="my-5">
                            <p class="text-2xl text-white">Game details</p>
                        </div>

                        <div class="text-gray-300 ">
                            <div class="flex">
                                <p class="font-bold">Release name:&nbsp;</p>
                                <p>{{this.name}}</p>
                            </div>
                            <div class="flex mb-5">
                                <p class="font-bold">Size:&nbsp;</p>
                                <p>{{this.sizeofgame.slice(5)}}</p>
                            </div>
                            <div class="flex">
                                <p class="font-bold">Title:&nbsp;</p>
                                <p>{{this.name}}</p>
                            </div>
                            <div class="flex">
                                <p class="font-bold">Genre:&nbsp;</p>
                                <p>{{this.genre}}</p>
                            </div>
                            <div class="flex">
                                <p class="font-bold">Gamemode:&nbsp;</p>
                                <p>{{this.gamemode}}</p>
                            </div>
                            <div class="flex">
                                <p class="font-bold">Developer:&nbsp;</p>
                                <p>{{this.devInfo[1]}}</p>
                            </div>
                            <div class="flex">
                                <p class="font-bold">Publisher:&nbsp;</p>
                                <p>{{this.devInfo[2]}}</p>
                            </div>
                            <div class="flex">
                                <p class="font-bold">Release Date:&nbsp;</p>
                                <p>{{this.releasedDate}}</p>
                            </div>

                            <div class="flex text-xl text-green-500 my-5">
                                <p>ALL Reviews:&nbsp;</p>
                                <p>{{this.devInfo[3]}}</p>
                            </div>

                            <div class="flex flex-col text-xl">
                                <p class="text-yellow-500">🙋‍♂ After reviewing the game, BUY the game to support the developer 👇</p>
                                <a :href="this.linkApi" class="text-red-500">{{this.linkApi}}</a>
                            </div>
                        </div>

                        <div class="flex flex-col justify-center my-5">
                            <div class="flex justify-center mb-3">
                                <p class="text-white text-3xl">Screenshots</p>
                            </div>

                            <div id="cf7" class="flex justify-center items-center">
                                <img :src="this.screenshots[0]" id="firstIMG" class="opaque">
                                <img :src="this.screenshots[1]" id="secondIMG">
                            </div>

                            <div class="flex justify-center gap-4 text-white text-3xl">
                                <img @click="selectScreenshot" id="firstSelect" class="cursor-pointer transform rotate-180" src="/img/arrow.png">
                                <img @click="selectScreenshot" id="secondSelect" class="cursor-pointer" src="/img/arrow.png">
                            </div>
                        </div>

                        <div v-if="hasTrailer" class="flex flex-col my-5">
                            <div class="flex justify-center mb-2">
                                <p class="text-white text-3xl">
                                    Trailer
                                </p>
                            </div>

                            <div class="player-container flex justify-center">

                                <iframe v-if="hasYTLink" class="w-full" height="345" :src="this.YTLink" ></iframe>
                                
                                <video v-else controls autoplay muted loop>
                                    <source :src="this.devInfo[4]" type="video/webm">
                                </video>
                            </div>
                        </div>

                        <!-- Main information about the games div -->
                        <div class="flex flex-col" id="aboutgame">
                            <div class="my-2">
                                <p class="text-white text-3xl mb-2">
                                    About this game
                                </p>
                                <p class="text-white text-gray-300">
                                    {{this.description}}
                                </p>
                            </div>

                            <div class="flex flex-col my-2">
                                <p class="text-white text-3xl">System requirements</p>
                                <div class="flex-col">
                                    <div class="flex">
                                        <p class="text-gray-300">{{this.systemReq[0]}}</p>
                                    </div>
                                    <div class="flex">
                                        <p class="text-gray-300">{{this.systemReq[1]}}</p>
                                    </div>
                                    <div class="flex">
                                        <p class="text-gray-300">{{this.systemReq[2]}}</p>
                                    </div>
                                    <div class="flex">
                                        <p class="text-gray-300">{{this.systemReq[3]}}</p>
                                    </div>
                                    <div class="flex">
                                        <p class="text-gray-300">{{this.systemReq[5]}}</p>
                                    </div>
                                </div>
                            </div>

                            <!-- Section for HOW TO INSTALL THE GAME -->
                            <div class="flex flex-col my-3">
                                <div class="mb-2">
                                    <p class="text-white text-3xl">How to install the game</p>
                                </div>

                                <div class="flex flex-col text-gray-300">
                                    <p>1) Download the game using a Torrent program or Direct program</p>
                                    <p>2) Extract the game to your preferred location with WinRar or 7-Zip</p>
                                    <p>3) Wait for the extraction to end</p>
                                    <p>4) No need to install the game, just start with the LAUNCHER of the game as administrator</p>
                                    <p>5) Play!</p>
                                </div>
                            </div>

                            <!-- Section for GENERAL NOTES: -->
                            <div class="flex flex-col my-5">
                                <div class="flex flex-col mb-2">
                                    <p class="text-white text-3xl">General Notes:</p>
                                </div>

                                <div class="flex flex-col text-gray-300">
                                    <p>– Make sure you have Spacewar installed. Windows Key + R and type (steam://install/480).</p>
                                    <p>– It is recommended to turn off your antivirus as some files get detected as false positive.</p>
                                    <p>– – Do not block the game with firewall if you are playing an online game with your friends.</p>
                                    <p>– In the case of an offline game, you may need to block it with firewall to prevent it from going online.</p>
                                    <p>– Turn Off your AntiVirus and Block the game’s exe in your firewall to prevent the game from trying to go online ..</p>
                                    <p>– If you install games to your system drive, it may be necessary to run this game with admin privileges instead</p>
                                </div>
                            </div>

                            <!-- Section for DOWNLOAD LINKS -->
                            <div class="flex flex-col my-5">
                                <div class="mb-3">
                                    <p class="text-white text-3xl">Download Game</p>
                                </div>

                                <div class="flex flex-col text-center justify-center">

                                    <div v-show="uploading" class="border-b-2 border-gray-300 pb-4 mb-4">
                                        <p class="text-blue-300 text-3xl mb-2">
                                            Uploading files...
                                        </p>
                                    </div>

                                    <div v-show="mediafireLink" class="border-b-2 border-gray-300 pb-4 mb-4">
                                        <p class="text-blue-300 text-3xl mb-2">
                                            Mediafire:
                                        </p>
                                        <div class="flex justify-center">
                                            <div class="flex justify-center border-2 bg-blue-500 w-2/5 cursor-pointer py-1">
                                                <img src="../../public/img/downloadbutton.png" class="border-r-2 border-gray-300 pr-4 mr-4">
                                                <a :href="mediafireDL" class="text-xl text-gray-200">
                                                    Download
                                                </a>
                                            </div>
                                        </div>
                                    </div>

                                    <div v-show="MEGALink" class="border-b-2 border-gray-300 pb-4 mb-4">
                                        <p class="text-red-300 text-3xl mb-2">
                                            MEGA:
                                        </p>
                                        <div class="flex justify-center">
                                            <div class="flex justify-center border-2 bg-blue-500 w-2/5 cursor-pointer py-1">
                                                <img src="../../public/img/downloadbutton.png" class="border-r-2 border-gray-300 pr-4 mr-4">
                                                <a :href="megaDL" class="text-xl text-gray-200">
                                                    Download
                                                </a>
                                            </div>
                                        </div>
                                    </div>

                                    <div v-show="BowfileLink" class="border-b-2 border-gray-300 pb-4 mb-4">
                                        <p class="text-purple-400 font-bold text-3xl mb-2">
                                            Bowfile:
                                        </p>
                                        <div class="flex justify-center">
                                            <div class="flex justify-center border-2 bg-blue-500 w-2/5 cursor-pointer py-1">
                                                <img src="../../public/img/downloadbutton.png" class="border-r-2 border-gray-300 pr-4 mr-4">
                                                <a :href="bowfileDL" class="text-xl text-gray-200">
                                                    Download
                                                </a>
                                            </div>
                                        </div>
                                    </div>

                                    <div v-show="TorrentLink" class="border-b-2 border-gray-300 pb-4 mb-4">
                                        <p class="text-green-300 text-3xl mb-2">
                                            TORRENT:
                                        </p>
                                        <div class="flex justify-center">
                                            <div class="flex justify-center border-2 bg-blue-500 w-2/5 cursor-pointer py-1">
                                                <img src="../../public/img/downloadbutton.png" class="border-r-2 border-gray-300 pr-4 mr-4">
                                                <a :href="torrentDL" class="text-xl text-gray-200">
                                                    Download
                                                </a>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>

                            <!--SECTION for Recommendations -->
                            <div>
                                <div>
                                    <p class="text-white text-3xl">Recommendations</p>
                                </div>
                                <div>
                                    <p class="text-gray-300 text-xl">In construction</p>
                                </div>

                            </div>

                            <!--SECTION for comments -->

                        </div>

                    </div>
                </div>

                <div class="w-2/5">
                    <div class="my-5">
                        <span class="font-kanit text-white text-3xl">Trending</span>
                    </div>

                    <div class="flex flex-col items-center mb-5">
                            <a class="w-4/5" href="http://localhost:8080/game/NM%20Hired%20Gun#top">
                                <img src="https://cdn.cloudflare.steamstatic.com/steam/apps/1222370/header.jpg?t=1624899675" class="">
                            </a>
                            <span class="mx-auto my-0 font-kanit text-white text-2xl">NM Hired Gun</span>
                        </div>

                        <div class="flex flex-col items-center mb-5">
                            <a class="w-4/5" href="http://localhost:8080/game/Aliens%20Fireteam%20Elite">
                                    <img src="https://cdn.cloudflare.steamstatic.com/steam/apps/1549970/header.jpg?t=1629799811" class="">
                                </a>
                            <span class="font-kanit text-white text-2xl">Aliens Fireteam Elite</span>
                        </div>

                        <div class="flex flex-col items-center mb-5">
                            <a class="w-4/5" href="http://localhost:8080/game/NM%20Hired%20Gun#top">
                                    <img src="https://cdn.cloudflare.steamstatic.com/steam/apps/1484900/header.jpg?t=1629812252" class="">
                                </a>
                            <span class="font-kanit text-white text-2xl">Hoa</span>
                        </div>
                        
                        <div class="flex flex-col items-center mb-5">
                            <a class="w-4/5" href="http://localhost:8080/game/Absolute%20Territory#top">
                                    <img src="https://cdn.cloudflare.steamstatic.com/steam/apps/1130880/header.jpg?t=1620641596" class="">
                                </a>
                            <span class="font-kanit text-white text-2xl">Absolute Territory</span>
                        </div>

                        <div class="flex flex-col items-center mb-5">
                            <a class="w-4/5" href="http://localhost:8080/game/Drift%20King">
                                    <img src="https://cdn.cloudflare.steamstatic.com/steam/apps/1469690/header.jpg?t=1629713717" class="">
                                </a>
                            <span class="font-kanit text-white text-2xl">Drift King</span>
                        </div>
                </div>
            </div>

        </div>
        
        <div class="w-full text-center text-white flex flex-col bg-gray-700">
            <span>Copyright © Game3rb</span>
            <span>By : Arab 4 Gamez</span>
      </div>
    </div>
</template>

<script>
import { jsonstr } from "../../declare.js"
// import { jsonstrUpdated } from "../../json.js"

export default {
    props:["name"],
    data () {
        return {
            uploading: false,
            searchbar: false,
            searchQuery: "",
            TorrentLink: true,
            mediafireLink: false,
            MEGALink: false,
            BowLink: false,
            gameClicked: "",
            gameList:[],
            currentPage:[],
            currentGameLinks:[],
            sizeofgame: "",
            releaseDate: "",
            linkApi: "",
            description: "",
            screenshots: "",
            genre: "",
            systemReq: "",
            gamemode: "Singleplayer",
            developers:"",
            devInfo:["Empty","Empty","Empty","Empty"],
            hasTrailer: false,
            hasYTLink: false,
            YTLink: "",
        }
    },

    methods: {
        selectScreenshot(event) {
            var element = document.getElementById("firstIMG")
            var secondElement = document.getElementById("secondIMG")

            if (event.srcElement.id == "firstSelect"){
                element.classList.remove("opaque")
                secondElement.classList.remove("opaque")
                element.classList.add("opaque")
            }else {
                console.log("here")
                element.classList.remove("opaque")
                secondElement.classList.remove("opaque")
                secondElement.classList.add("opaque")
            }
        },

        downloadFunc: function(content, fileName, contentType) {
            var a = document.createElement("a");
            var file = new Blob([content], {type: contentType});
            a.href = URL.createObjectURL(file);
            a.download = fileName;
            a.click();
        },
    },

    // mounted() {
    //     var currentgame = this.name
    //     var element1Changed = this.gameList.map(function (element) {
    //         element.map(function (el) {
    //             if (el == currentgame) {
    //                 console.log(element[1])
    //                 var updatedGameClicks = element[1].split("|")
    //                 updatedGameClicks[9] = String(parseInt(updatedGameClicks[9]) + 1)
    //                 element[1] = updatedGameClicks.join("|")
    //             }
    //         })
    //         return element
    //     })
        
    //     console.log(jsonstrUpdated)

    //     // var newElement = JSON.stringify(element1Changed)
    //     var jsonData = "export var jsonstrUpdated = " +  JSON.stringify(element1Changed)
    //     this.downloadFunc(jsonData, 'json.js', 'text/plain')
    // },

    created() {
        async function postData(url = '', fields =' ') {
        // Default options are marked with *
        const response = await fetch(url, {
            method: 'POST', // *GET, POST, PUT, DELETE, etc.
            mode: 'cors', // no-cors, *cors, same-origin
            headers: {
            'Content-Type': 'application/json',
            'Client-ID': 'x791m08fo4a05ewa5m869cm2ihvzw8',
            'Authorization': 'Bearer xbi3q6up891wjbshw15438e88kpb8s',
            'origin': 'x-requested-with',
            },
            body: fields // body data type must match "Content-Type" header
        });
            return response.json(); // parses JSON response into native JavaScript objects
        }

        this.gameList = Object.entries(jsonstr)
        this.currentPage = this.gameList.slice(0,20)
        var currentgame = this.name
        var releaseDateArr = this.releaseDate
        var descriptionArr = this.description
        var linkApiArr = this.linkApi
        var sysReqArr = this.systemReq
        var screenshotsArr = this.screenshots
        var genreArr = this.genre
        var downloadLinksArr = this.currentGameLinks
        var sizeofgame = this.sizeofgame
        var developersArr = this.developers
        var gameClicked = this.gameClicked
        var YTLinkArr = this.YTLink
        this.gameList.map(function (element) {
            element.map(function (el) {
                if (el == currentgame) {
                    downloadLinksArr = element[1].split("|")[0].split("$$")
                    sysReqArr = element[1].split("|")[1].split("$$")
                    sizeofgame = element[1].substr(element[1].lastIndexOf('|') + 1)
                    releaseDateArr = element[1].split("|")[3].slice(13)
                    linkApiArr = element[1].split("|")[6]
                    genreArr = element[1].split("|")[2].slice(6)
                    descriptionArr = element[1].split("|")[4]
                    screenshotsArr = element[1].split("|")[5].split("$$")
                    developersArr = element[1].split("|")[7].split("$$")
                    gameClicked = element[1].split("|")[9]
                    YTLinkArr = element[1].split("|")[8]
                    console.log(YTLinkArr);
                }
            })
        })

        this.developers = developersArr

        if(this.developers[0] == "Empty") {
            var searchString = 'search ' + `"${this.name}"` + '; fields id;'
            postData('https://cors-anywhere.herokuapp.com/https://api.igdb.com/v4/games?', searchString)
            .then(responseFromApi => {
                var idSearchedGame = 'fields *;' + 'where game = ' + `${responseFromApi[0].id}` + ';'
                postData('https://cors-anywhere.herokuapp.com/https://api.igdb.com/v4/covers?',  idSearchedGame)
                    .then(screenshotApi => {
                        this.devInfo[0] = screenshotApi[0].url.replace("t_thumb", "t_cover_big").replace("//", "https:/")
                        console.log(screenshotApi)
                    })
                
                this.devInfo[1] = "TBA"
                this.devInfo[2] = "TBA"
                this.devInfo[3] = "TBA"
                this.devInfo[4] = "TBA"
                this.devInfo[5] = "TBA"
                this.hasTrailer = false
            });
        }else{
            this.devInfo[0] = this.developers[0]
            this.devInfo[1] = this.developers[1]
            this.devInfo[2] = this.developers[2]
            this.devInfo[3] = this.developers[3]
            this.devInfo[4] = this.developers[4]
            this.devInfo[5] = this.developers[5]
            this.hasTrailer = true
            console.log((this.devInfo))
        }


        for (var i= 0; i< this.devInfo.length; i++) {
            if (this.devInfo[i] == "Online") {
                this.gamemode = "Online"
            }
        }
        
        if (this.devInfo[4] == undefined) {
            this.devInfo[4] == "Empty"
            this.hasYTLink = true
        }else {
            if (!(this.devInfo[4].includes("steam"))) {
                this.hasYTLink = true
            }else {
                this.hasYTLink = false
            }
        }


        var mediafireDL = ""
        var bowfileDL = ""
        var megaDL = ""
        var torrentDL = ""
        var mediafireLink = false
        var BowfileLink = false
        var MEGALink = false
        var TorrentLink = false
        downloadLinksArr.map(function (element) {
            //console.log(element)
            if (element.includes("mediafire")) {
                mediafireLink = true
                mediafireDL = element
            }else if (element.includes("bowfile")) {
                BowfileLink = true
                bowfileDL = element
            }else if (element.includes("MEGA")) {
                MEGALink = true
                megaDL = element
            }else if (element.includes("zippy")) {
                TorrentLink = true
                torrentDL = element
            }
        })

        this.mediafireDL = mediafireDL
        this.bowfileDL = bowfileDL
        this.megaDL = megaDL
        this.torrentDL = torrentDL
        this.MEGALink = MEGALink
        this.TorrentLink = TorrentLink
        this.BowfileLink =  BowfileLink
        this.mediafireLink = mediafireLink
        this.YTLink = YTLinkArr
        this.genre = genreArr
        this.currentGameLinks = downloadLinksArr
        this.systemReq = sysReqArr
        this.releasedDate = releaseDateArr
        this.description = descriptionArr
        this.linkApi = linkApiArr
        this.gameClicked = parseInt(gameClicked) + 1
        this.screenshots = screenshotsArr
        this.sizeofgame = sizeofgame

        if (this.currentGameLinks[0] == "" ) {
            this.uploading = true
        }

        console.log(this.currentGameLinks)
        
    }
}
</script>

<style>

#cf7 {
  position:relative;
  height:281px;
  width:450px;
  margin:0 auto 10px;
}
#cf7 img {
  position:absolute;
  left:0;
  -webkit-transition: opacity 1s ease-in-out;
  -moz-transition: opacity 1s ease-in-out;
  -o-transition: opacity 1s ease-in-out;
  transition: opacity 1s ease-in-out;
  opacity:0;
  -ms-filter:"progid:DXImageTransform.Microsoft.Alpha(Opacity=0)";
  filter: alpha(opacity=0);
}

#cf7 img.opaque {
  opacity:1;
  -ms-filter:"progid:DXImageTransform.Microsoft.Alpha(Opacity=100)";
  filter: alpha(opacity=1);
}


</style>
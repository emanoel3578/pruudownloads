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
                            <input v-on:keyup.enter="sendSearch" v-model="searchQuery" v-show="searchbar" class="text-black" size="25">
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
                    <li @mouseover ="categoriesHover = true" @mouseleave ="categoriesHover = false" class="bg-white rounded-full border-2 border-black cursor-pointer hover:bg-purple-500 p-2 m-2 relative">
                        <div class="">
                            <a class="">Categories</a>
                        </div>
                        <div v-show="categoriesHover" class="z-10 border-2 border-black font-kanit cursor-default flex absolute text-white bg-purple-500 gap-5 rounded-lg">
                            <ul class="m-3 ">
                                <li class="cursor-pointer mb-1 mx-2 hover:text-black"><a href="http://localhost:8080/search/s=Singleplayer">Singleplayer</a></li>
                                <li class="cursor-pointer mb-1 mx-2 hover:text-black"><a href="http://localhost:8080/search/s=Multiplayer">Multiplayer</a></li>
                                <li class="cursor-pointer mb-1 mx-2 hover:text-black"><a href="http://localhost:8080/search/s=Indie">Indie</a></li>
                                <li class="cursor-pointer mb-1 mx-2 hover:text-black"><a href="http://localhost:8080/search/s=Action">Action</a></li>
                                <li class="cursor-pointer mb-1 mx-2 hover:text-black"><a href="http://localhost:8080/search/s=Adventure">Adventure</a></li>
                                <li class="cursor-pointer mb-1 mx-2 hover:text-black"><a href="http://localhost:8080/search/s=Casual">Casual</a></li>
                                <li class="cursor-pointer mb-1 mx-2 hover:text-black"><a href="http://localhost:8080/search/s=Simulation">Simulation</a></li>
                                <li class="cursor-pointer mb-1 mx-2 hover:text-black"><a href="http://localhost:8080/search/s=RPG">RPG</a></li>
                            </ul>

                            <ul class="m-3">
                                <li class="cursor-pointer mb-1 mx-2 hover:text-black"><a href="http://localhost:8080/search/s=2D">2D</a></li>
                                <li class="cursor-pointer mb-1 mx-2 hover:text-black"><a href="http://localhost:8080/search/s=Atmospheric">Atmospheric</a></li>
                                <li class="cursor-pointer mb-1 mx-2 hover:text-black"><a href="http://localhost:8080/search/s=Puzzle">Puzzle</a></li>
                                <li class="cursor-pointer mb-1 mx-2 hover:text-black"><a href="http://localhost:8080/search/s=Strategy">Strategy</a></li>
                                <li class="cursor-pointer mb-1 mx-2 hover:text-black"><a href="http://localhost:8080/search/s=Pixel">Pixel</a></li>
                                <li class="cursor-pointer mb-1 mx-2 hover:text-black"><a href="http://localhost:8080/search/s=Fantasy">Fantasy</a></li>
                                <li class="cursor-pointer mb-1 mx-2 hover:text-black"><a href="http://localhost:8080/search/s=Colorful">Colorful</a></li>
                            </ul>
                        </div>
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
                <div v-for="item in apidata" :key='item.index' class="flex flex-col w-full">
                    <div class="flex text-white mb-5">
                        <div class="border-2 border-black bg-gray-800 px-3">
                            <a>{{(item.genre).replace('Genre: ', "")}}</a>
                        </div>
                    </div>

                    <div class="flex flex-col text-white">
                        <div class="flex">
                            <p class="text-3xl">Download&nbsp;</p>
                            <p class="text-3xl">{{item.name}}</p>
                        </div>
                        <div class="flex mt-5">
                            <p>about&nbsp;</p>
                            <p>:time:</p>
                        </div>
                    </div>

                    <div class="flex justify-center">
                        <img :src="item.imgheader" class="w-3/5 max-h-auto">
                    </div>

                    <div class="flex flex-col ">
                        <div class="my-5">
                            <p class="text-2xl text-white">Game details</p>
                        </div>

                        <div class="text-gray-300 ">
                            <div class="flex">
                                <p class="font-bold">Release name:&nbsp;</p>
                                <p>{{item.nameref}}</p>
                            </div>
                            <div class="flex mb-5">
                                <p class="font-bold">Size:&nbsp;</p>
                                <p>{{item.size.slice(5)}}</p>
                            </div>
                            <div class="flex">
                                <p class="font-bold">Title:&nbsp;</p>
                                <p>{{item.name}}</p>
                            </div>
                            <div class="flex">
                                <p class="font-bold">Genre:&nbsp;</p>
                                <p>{{(item.genre).replace('Genre: ', "")}}</p>
                            </div>
                            <div class="flex">
                                <p class="font-bold">Gamemode:&nbsp;</p>
                                <p>{{item.gamemode}}</p>
                            </div>
                            <div class="flex">
                                <p class="font-bold">Developer:&nbsp;</p>
                                <p>{{item.developer}}</p>
                            </div>
                            <div class="flex">
                                <p class="font-bold">Publisher:&nbsp;</p>
                                <p>{{item.publisher}}</p>
                            </div>
                            <div class="flex">
                                <p class="font-bold">Release Date:&nbsp;</p>
                                <p>{{item.releasedate}}</p>
                            </div>

                            <div class="flex text-xl text-green-500 my-5">
                                <p>ALL Reviews:&nbsp;</p>
                                <p>{{item.ratings}}</p>
                            </div>

                            <div class="flex flex-col text-xl">
                                <p class="text-yellow-500">🙋‍♂ After reviewing the game, BUY the game to support the developer 👇</p>
                                <a :href="item.pagelink" class="text-red-500">{{item.pagelink}}</a>
                            </div>
                        </div>

                        <div class="flex flex-col justify-center my-5">
                            <div class="flex justify-center mb-3">
                                <p class="text-white text-3xl">Screenshots</p>
                            </div>

                            <div id="cf7" class="flex justify-center items-center">
                                <img :src="item.img1" id="firstIMG" class="opaque">
                                <img :src="item.img2" id="secondIMG">
                            </div>

                            <div class="flex justify-center gap-4 text-white text-3xl">
                                <img @click="selectScreenshot" id="firstSelect" class="cursor-pointer transform rotate-180" src="/img/arrow.png">
                                <img @click="selectScreenshot" id="secondSelect" class="cursor-pointer" src="/img/arrow.png">
                            </div>
                        </div>

                        <div class="flex flex-col my-5">
                            <div class="flex justify-center mb-2">
                                <p class="text-white text-3xl">
                                    Trailer
                                </p>
                            </div>

                            <div class="player-container flex justify-center">
                                <iframe v-if="hasYTLink" class="w-full" height="345" :src="item.ytLink" ></iframe>
                                
                                <video v-else controls autoplay muted loop>
                                    <source :src="item.videolink" type="video/webm">
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
                                    {{item.description}}
                                </p>
                            </div>

                            <div class="flex flex-col my-2">
                                <p class="text-white text-3xl">System requirements</p>
                                <div class="flex-col">
                                    <div class="flex">
                                        <p class="text-gray-300">{{item.sys_requirements}}</p>
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

                                    <div v-if="isOnline">
                                        <div class="border-b-2 border-gray-300 pb-4 mb-4">
                                            <p class="text-green-300 text-3xl mb-2">
                                                Full Game:
                                            </p>
                                            <div class="flex justify-center">
                                                <div id="DownloadButton" @click="hideLinksFullGame" class="flex justify-center borderBottom border-t-2 border-r-2 border-l-2 bg-blue-500 w-2/5 cursor-pointer py-1">
                                                    <img src="../../public/img/downloadbutton.png" class="border-r-2 border-gray-300 pr-4 mr-4">
                                                    <a class="text-xl text-gray-200">
                                                        Download
                                                    </a>
                                                </div>
                                            </div>

                                            <div v-show="showFullGameLinks" class="bg-blue-500 border-2 w-4/5 text-white mx-auto my-0 rounded-lg ">
                                                <div class="flex flex-col mx-auto my-0">
                                                    <div class="flex flex-col mx-auto my-0 w-min gap-1">
                                                        <div class="mt-2">
                                                            <a class="cursor-pointer">https://bowfile.com/asdaasdsdasdasdasdasdassdasd</a>
                                                        </div>

                                                        <div>
                                                            <a class="cursor-pointer">https://bowfile.com/1LuA</a>
                                                        </div>

                                                        <div>
                                                            <a class="cursor-pointer">https://bowfile.com/1LuA</a>
                                                        </div>

                                                        <div>
                                                            <a class="cursor-pointer">https://bowfile.com/1LuA</a>
                                                        </div>

                                                        <div>
                                                            <a class="cursor-pointer">https://bowfile.com/1LuA</a>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>

                                        <div v-show="mediafireLink" class="border-b-2 border-gray-300 pb-4 mb-4">
                                            <p class="text-red-500 text-3xl mb-2">
                                                Online fix:
                                            </p>
                                            <div class="flex justify-center">
                                                <div id="DownloadButtonFix" @click="hideLinksOnlineFixGame" class="flex justify-center borderBottom border-t-2 border-r-2 border-l-2 bg-blue-500 w-2/5 cursor-pointer py-1">
                                                    <img src="../../public/img/downloadbutton.png" class="border-r-2 border-gray-300 pr-4 mr-4">
                                                    <a class="text-xl text-gray-200">
                                                        Download
                                                    </a>
                                                </div>
                                            </div>

                                            <div v-show="showOnlineFixLinks" class="bg-blue-500 border-2 w-4/5 text-white mx-auto my-0 rounded-lg ">
                                                <div class="flex flex-col mx-auto my-0">
                                                    <div class="flex flex-col mx-auto my-0 w-min gap-1">
                                                        <div class="mt-2">
                                                            <a class="cursor-pointer">https://bowfile.com/asdaasdsdasdasdasdasdassdasd</a>
                                                        </div>

                                                        <div>
                                                            <a class="cursor-pointer">https://bowfile.com/1LuA</a>
                                                        </div>

                                                        <div>
                                                            <a class="cursor-pointer">https://bowfile.com/1LuA</a>
                                                        </div>

                                                        <div>
                                                            <a class="cursor-pointer">https://bowfile.com/1LuA</a>
                                                        </div>

                                                        <div>
                                                            <a class="cursor-pointer">https://bowfile.com/1LuA</a>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>


                                        </div>
                                    </div>

                                    <div v-else>
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
                            </div>

                            <!--SECTION for Recommendations 
                            <div>
                                <div>
                                    <p class="text-white text-3xl">Recommendations</p>
                                </div>
                                <div>
                                    <p class="text-gray-300 text-xl">In construction</p>
                                </div>

                            </div>-->

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
export default {
    props:["id"],
    data () {
        return {
            showOnlineFixLinks: false,
            showFullGameLinks: false,
            isOnline: true,
            categoriesHover: false,
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
            hasYTLink: false,
            YTLink: "",
            apidata:[],
        }
    },

    methods: {
        
        hideLinksFullGame() {
            document.getElementById("DownloadButton").classList.toggle("borderBottom")
            this.showFullGameLinks = !this.showFullGameLinks
        },

        hideLinksOnlineFixGame() {
            document.getElementById("DownloadButtonFix").classList.toggle("borderBottom")
            this.showOnlineFixLinks = !this.showOnlineFixLinks
        },

        selectScreenshot(event) {
            var element = document.getElementById("firstIMG")
            var secondElement = document.getElementById("secondIMG")

            if (event.srcElement.id == "firstSelect"){
                element.classList.remove("opaque")
                secondElement.classList.remove("opaque")
                element.classList.add("opaque")
            }else {
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

    created() {
        this.axios.get('http://127.0.0.1:8000/api/game/'+this.id).then((response)=>{
            this.apidata = response.data;
            this.LoadMainCards = false
            if (response.data.Result.videolink == null) {
                this.hasYTLink = true
            }
            console.log(response.data.Result)
        })
    }
}
</script>

<style>

.borderBottom{
    border-bottom-width: 2px;
}

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